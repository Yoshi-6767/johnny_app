import json
import smtplib
import random
from datetime import date, timedelta
from email.mime.text import MIMEText

from flask_login import current_user

from config import Config
from models import db, LearnedWord, WordProgress
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


# ─── СЛОВА ───

WORDS_FILE = "words.json"
try:
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        COMMON_WORDS = json.load(f)
except Exception:
    COMMON_WORDS = {}


def get_user_general_words(user_id):
    """Свои слова юзера (категория general). Хранятся в памяти — это временно."""
    return _USERS_MEMORY.setdefault(user_id, {}).setdefault("general_words", {})


def get_user_phrases(user_id):
    return _USERS_MEMORY.setdefault(user_id, {}).setdefault("phrases", {})


def get_user_topics(user_id):
    return _USERS_MEMORY.setdefault(user_id, {}).setdefault("topics", {})


def get_user_exams(user_id):
    return _USERS_MEMORY.setdefault(user_id, {}).setdefault("exams", {})


def get_user_progress(user_id):
    data = _USERS_MEMORY.setdefault(user_id, {}).setdefault("progress", {})
    if not data:
        data.update({"history": [], "streak": 0, "last_day": "", "weak_words": {}})
    return data


# Временное хранилище (как было). Позже переедет в БД.
_USERS_MEMORY = {}


def get_all_words(user_id):
    """Общие слова + свои слова юзера."""
    all_w = dict(COMMON_WORDS)
    all_w.update(get_user_general_words(user_id))
    return all_w


# ─── LEARNED ───

def get_learned_words(user_id):
    """Множество выученных слов юзера."""
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
    """Счётчик правильных подряд. При достижении порога — learned."""
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
    """Сброс стрика по слову."""
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


# ─── ПРОГРЕСС ───

def record_training(correct: bool, word=None):
    """Записывает результат в историю, стрик, слабые слова.
       Всё ещё в памяти — потом переедет в БД."""
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


# ─── КАТЕГОРИИ ───

def get_section_stats(user_id, section_id):
    """Возвращает: total, learned, is_passed (по экзамену), exam_passed."""
    if section_id == "general":
        section_words = get_user_general_words(user_id)
    else:
        section_words = {k: v for k, v in COMMON_WORDS.items() if v.get("section") == section_id}

    total = len(section_words)
    learned_set = get_learned_words(user_id)
    learned = sum(1 for w in section_words if w in learned_set)

    return {"total": total, "learned": learned}
