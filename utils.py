import json
import smtplib
from datetime import date, timedelta
from email.mime.text import MIMEText

from flask_login import current_user

from config import Config
from models import (
    db, LearnedWord, WordProgress,
    UserWord, UserPhrase, UserTopic, UserExam, UserProgress,
)
from data import SECTIONS, get_section


# ─── SMTP ───

def send_verification_code(to_email, code):
    msg = MIMEText(f"Твой код подтверждения: {code}\n\nКод действует 15 минут.")
    msg['Subject'] = 'Подтверждение регистрации — Flow & Word'
    msg['From'] = Config.SMTP_USER
    msg['To'] = to_email

    server = smtplib.SMTP(Config.SMTP_SERVER, Config.SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(Config.SMTP_USER, Config.SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()


# ─── ОБЩИЕ СЛОВА ───

WORDS_FILE = "words.json"
try:
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        COMMON_WORDS = json.load(f)
except Exception:
    COMMON_WORDS = {}


# ═══════════════════════════════════════════════
# СВОИ СЛОВА ЮЗЕРА (UserWord)
# ═══════════════════════════════════════════════

def get_user_general_words(user_id):
    """Возвращает dict {eng: {rus, section}} — как было раньше."""
    rows = UserWord.query.filter_by(user_id=user_id).all()
    return {r.eng: {"rus": r.rus, "section": r.section} for r in rows}


def add_user_word(user_id, eng, rus, section='general'):
    exists = UserWord.query.filter_by(user_id=user_id, eng=eng).first()
    if exists:
        exists.rus = rus
        exists.section = section
    else:
        db.session.add(UserWord(user_id=user_id, eng=eng, rus=rus, section=section))
    db.session.commit()


def delete_user_word(user_id, eng):
    row = UserWord.query.filter_by(user_id=user_id, eng=eng).first()
    if row:
        db.session.delete(row)
        db.session.commit()


def edit_user_word(user_id, old_eng, new_eng, new_rus):
    row = UserWord.query.filter_by(user_id=user_id, eng=old_eng).first()
    if row:
        row.eng = new_eng
        row.rus = new_rus
        db.session.commit()


# ═══════════════════════════════════════════════
# ФРАЗЫ (UserPhrase)
# ═══════════════════════════════════════════════

def get_user_phrases(user_id):
    rows = UserPhrase.query.filter_by(user_id=user_id).all()
    return {r.eng: r.rus for r in rows}


def add_user_phrase(user_id, eng, rus):
    exists = UserPhrase.query.filter_by(user_id=user_id, eng=eng).first()
    if exists:
        exists.rus = rus
    else:
        db.session.add(UserPhrase(user_id=user_id, eng=eng, rus=rus))
    db.session.commit()


def delete_user_phrase(user_id, eng):
    row = UserPhrase.query.filter_by(user_id=user_id, eng=eng).first()
    if row:
        db.session.delete(row)
        db.session.commit()


def edit_user_phrase(user_id, old_eng, new_eng, new_rus):
    row = UserPhrase.query.filter_by(user_id=user_id, eng=old_eng).first()
    if row:
        row.eng = new_eng
        row.rus = new_rus
        db.session.commit()


# ═══════════════════════════════════════════════
# ТОПИКИ (UserTopic)
# ═══════════════════════════════════════════════

def get_user_topics(user_id):
    """Возвращает dict {topic_id: {title, text, done}}."""
    rows = UserTopic.query.filter_by(user_id=user_id).all()
    return {r.topic_id: {"title": r.title, "text": r.text, "done": r.is_done} for r in rows}


def save_user_topic(user_id, topic_id, title, text, is_done):
    row = UserTopic.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if row:
        row.title = title
        row.text = text
        row.is_done = is_done
    else:
        db.session.add(UserTopic(user_id=user_id, topic_id=topic_id, title=title, text=text, is_done=is_done))
    db.session.commit()


def create_user_topic(user_id, topic_id, title):
    row = UserTopic.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if not row:
        db.session.add(UserTopic(user_id=user_id, topic_id=topic_id, title=title, text='', is_done=False))
        db.session.commit()


def delete_user_topic(user_id, topic_id):
    row = UserTopic.query.filter_by(user_id=user_id, topic_id=topic_id).first()
    if row:
        db.session.delete(row)
        db.session.commit()


# ═══════════════════════════════════════════════
# ЭКЗАМЕНЫ-ТЕКСТЫ (UserExam)
# ═══════════════════════════════════════════════

def get_user_exams(user_id):
    """Возвращает dict {exam_id: {topic_id, title, text, date, word_count}}."""
    rows = UserExam.query.filter_by(user_id=user_id).order_by(UserExam.created_at.desc()).all()
    result = {}
    for r in rows:
        result[r.exam_id] = {
            "topic_id": r.topic_id,
            "title": r.title,
            "text": r.text,
            "date": r.created_at.strftime("%Y-%m-%d") if r.created_at else "",
            "word_count": r.word_count,
        }
    return result


def save_user_exam(user_id, exam_id, topic_id, title, text, word_count):
    db.session.add(UserExam(
        user_id=user_id, exam_id=exam_id, topic_id=topic_id,
        title=title, text=text, word_count=word_count,
    ))
    db.session.commit()


# ═══════════════════════════════════════════════
# ПРОГРЕСС (UserProgress)
# ═══════════════════════════════════════════════

def _get_or_create_progress(user_id):
    row = UserProgress.query.filter_by(user_id=user_id).first()
    if not row:
        row = UserProgress(user_id=user_id, streak=0, last_day='', history_json='[]', weak_words_json='{}')
        db.session.add(row)
        db.session.commit()
    return row


def get_user_progress(user_id):
    """Возвращает dict {history, streak, last_day, weak_words} — как раньше."""
    row = _get_or_create_progress(user_id)
    try:
        history = json.loads(row.history_json or '[]')
    except Exception:
        history = []
    try:
        weak_words = json.loads(row.weak_words_json or '{}')
    except Exception:
        weak_words = {}
    return {
        "history": history,
        "streak": row.streak or 0,
        "last_day": row.last_day or "",
        "weak_words": weak_words,
    }


def _save_progress_dict(user_id, progress_dict):
    row = _get_or_create_progress(user_id)
    row.streak = progress_dict.get("streak", 0)
    row.last_day = progress_dict.get("last_day", "")
    row.history_json = json.dumps(progress_dict.get("history", []), ensure_ascii=False)
    row.weak_words_json = json.dumps(progress_dict.get("weak_words", {}), ensure_ascii=False)
    db.session.commit()


# ═══════════════════════════════════════════════
# ОБЪЕДИНЁННЫЙ СПИСОК СЛОВ
# ═══════════════════════════════════════════════

def get_all_words(user_id):
    all_w = dict(COMMON_WORDS)
    all_w.update(get_user_general_words(user_id))
    return all_w


# ═══════════════════════════════════════════════
# LEARNED
# ═══════════════════════════════════════════════

def get_learned_words(user_id):
    rows = LearnedWord.query.filter_by(user_id=user_id).all()
    return {r.word for r in rows}


def is_learned(user_id, word):
    return LearnedWord.query.filter_by(user_id=user_id, word=word).first() is not None


def mark_learned(user_id, word, section):
    if is_learned(user_id, word):
        return
    db.session.add(LearnedWord(user_id=user_id, word=word, section=section))
    db.session.commit()


def unmark_learned(user_id, word):
    row = LearnedWord.query.filter_by(user_id=user_id, word=word).first()
    if row:
        db.session.delete(row)
        db.session.commit()


def register_correct_answer(user_id, word):
    row = WordProgress.query.filter_by(user_id=user_id, word=word).first()
    if not row:
        row = WordProgress(user_id=user_id, word=word, correct_streak=0)
        db.session.add(row)

    row.correct_streak = (row.correct_streak or 0) + 1

    if row.correct_streak >= Config.LEARNED_THRESHOLD:
        section = _find_section_for_word(user_id, word)
        mark_learned(user_id, word, section)

    db.session.commit()


def register_wrong_answer(user_id, word):
    row = WordProgress.query.filter_by(user_id=user_id, word=word).first()
    if row:
        row.correct_streak = 0
        db.session.commit()


def _find_section_for_word(user_id, word):
    if word in COMMON_WORDS:
        return COMMON_WORDS[word].get("section", "general")
    gw = get_user_general_words(user_id)
    if word in gw:
        return gw[word].get("section", "general")
    return "general"


# ═══════════════════════════════════════════════
# ЗАПИСЬ ТРЕНИРОВКИ
# ═══════════════════════════════════════════════

def record_training(correct: bool, word=None):
    if not current_user.is_authenticated:
        return
    uid = current_user.id
    progress = get_user_progress(uid)
    today = str(date.today())

    if progress.get("last_day") != today:
        yesterday = str(date.today() - timedelta(days=1))
        if progress.get("last_day") == yesterday:
            progress["streak"] = progress.get("streak", 0) + 1
        else:
            progress["streak"] = 1
        progress["last_day"] = today

    if not progress.get("history") or progress["history"][-1]["date"] != today:
        progress["history"].append({"date": today, "correct": 0, "wrong": 0})

    if correct:
        progress["history"][-1]["correct"] += 1
        if word:
            register_correct_answer(uid, word)
    else:
        progress["history"][-1]["wrong"] += 1
        if word:
            weak = progress.setdefault("weak_words", {})
            weak[word] = weak.get(word, 0) + 1
            register_wrong_answer(uid, word)

    _save_progress_dict(uid, progress)


# ═══════════════════════════════════════════════
# СТАТИСТИКА КАТЕГОРИИ
# ═══════════════════════════════════════════════

def get_section_stats(user_id, section_id):
    if section_id == "general":
        section_words = get_user_general_words(user_id)
    else:
        section_words = {k: v for k, v in COMMON_WORDS.items() if v.get("section") == section_id}

    total = len(section_words)
    learned_set = get_learned_words(user_id)
    learned = sum(1 for w in section_words if w in learned_set)

    return {"total": total, "learned": learned}
