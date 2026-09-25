from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response, send_from_directory
import json
import random
import os
import time
from datetime import date, timedelta, datetime
from deep_translator import MyMemoryTranslator
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from config import Config
from models import db, User, EmailCode, LearnedWord, WordProgress, SectionExam, Achievement, Goal
from data import SECTIONS, QUOTES, IRREGULAR_VERBS, PHRASAL_VERBS, IDIOMS, FIXED_TOPICS, get_section
from utils import (
    send_verification_code, COMMON_WORDS,
    get_user_general_words, add_user_word, delete_user_word, edit_user_word,
    get_user_phrases, add_user_phrase, delete_user_phrase, edit_user_phrase,
    get_user_topics, save_user_topic, create_user_topic, delete_user_topic,
    get_user_exams, save_user_exam,
    get_user_progress,
    get_all_words, get_learned_words, is_learned, mark_learned, unmark_learned,
    record_training, get_section_stats,
)
from achievements import (
    ACHIEVEMENTS, get_achievement, get_unlocked_codes, unlock,
    check_all as check_all_achievements,
)

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

if not os.path.exists(app.config['AVATAR_FOLDER']):
    os.makedirs(app.config['AVATAR_FOLDER'])

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


# ═══════════════════════════════════════════════
# ХЕЛПЕРЫ
# ═══════════════════════════════════════════════

def get_daily_quote():
    today = date.today()
    day_of_year = today.timetuple().tm_yday
    return QUOTES[day_of_year % len(QUOTES)]


def check_user_achievements(uid):
    progress = get_user_progress(uid)
    gw = get_user_general_words(uid)
    phrases = get_user_phrases(uid)
    topics = get_user_topics(uid)
    topics_done = sum(1 for t in topics.values() if t.get("done"))
    exams_count = SectionExam.query.filter_by(user_id=uid, is_passed=True).count()
    learned_count = LearnedWord.query.filter_by(user_id=uid).count()

    return check_all_achievements(
        user_id=uid,
        progress=progress,
        general_words_count=len(gw),
        phrases_count=len(phrases),
        topics_done=topics_done,
        exams_count=exams_count,
        learned_count=learned_count,
        games_stats={},
        study_stats={},
    )


def pop_new_achievements():
    codes = session.pop("new_achievements", [])
    return [get_achievement(c) for c in codes if get_achievement(c)]


# ═══════════════════════════════════════════════
# ГЛАВНАЯ
# ═══════════════════════════════════════════════

@app.route("/")
def index():
    new_achievements = pop_new_achievements()

    if current_user.is_authenticated:
        uid = current_user.id
        all_w = get_all_words(uid)
        total_words = len(all_w)
        total_phrases = len(get_user_phrases(uid))
        topics = get_user_topics(uid)
        total_topics_done = sum(1 for t in topics.values() if t.get("done"))
        total_topics = len(FIXED_TOPICS) + sum(1 for t in topics.keys() if t.startswith("custom_"))
        progress = get_user_progress(uid)
        streak = progress.get("streak", 0)

        weak_words = progress.get("weak_words", {})
        weak_sorted = sorted(weak_words.items(), key=lambda x: x[1], reverse=True)[:5]
        weak_list = []
        for w, count in weak_sorted:
            if w in all_w:
                weak_list.append({"word": w, "rus": all_w[w]["rus"], "count": count})

        today_str = str(date.today())
        today_correct = 0
        if progress.get("history") and progress["history"][-1]["date"] == today_str:
            today_correct = progress["history"][-1]["correct"]

        daily_goal = 10
        daily_percent = min(100, int(today_correct / daily_goal * 100))
        daily_done = today_correct >= daily_goal

        goals = Goal.query.filter_by(user_id=uid, is_completed=False).order_by(Goal.created_at.desc()).limit(2).all()
        goals_data = []
        for g in goals:
            if g.goal_type == "words":
                current = len(all_w)
            elif g.goal_type == "streak":
                current = streak
            else:
                current = 0
            percent = min(100, int(current / g.target * 100)) if g.target > 0 else 0
            goals_data.append({"id": g.id, "goal_type": g.goal_type, "target": g.target, "current": current, "percent": percent})
    else:
        total_words = len(COMMON_WORDS)
        total_phrases = 0
        total_topics_done = 0
        total_topics = len(FIXED_TOPICS)
        streak = 0
        weak_list = []
        today_correct = 0
        daily_goal = 10
        daily_percent = 0
        daily_done = False
        goals_data = []

    return render_template(
        "index.html",
        total_words=total_words,
        total_phrases=total_phrases,
        total_topics_done=total_topics_done,
        total_topics=total_topics,
        streak=streak,
        weak_list=weak_list,
        today_correct=today_correct,
        daily_goal=daily_goal,
        daily_percent=daily_percent,
        daily_done=daily_done,
        goals=goals_data,
        quote=get_daily_quote(),
        new_achievements=new_achievements,
    )


# ═══════════════════════════════════════════════
# АВАТАР И ПРОФИЛЬ
# ═══════════════════════════════════════════════

@app.route("/avatars/<filename>")
def avatar_file(filename):
    return send_from_directory(app.config['AVATAR_FOLDER'], filename)


@app.route("/profile")
@login_required
def profile():
    uid = current_user.id
    check_user_achievements(uid)

    all_w = get_all_words(uid)
    progress = get_user_progress(uid)
    unlocked = get_unlocked_codes(uid)

    rows = Achievement.query.filter_by(user_id=uid).order_by(Achievement.unlocked_at.desc()).limit(6).all()
    recent_ach = [get_achievement(r.code) for r in rows if get_achievement(r.code)]

    goals = Goal.query.filter_by(user_id=uid, is_completed=False).order_by(Goal.created_at.desc()).limit(3).all()
    goals_data = []
    for g in goals:
        if g.goal_type == "words":
            current = len(all_w)
        elif g.goal_type == "streak":
            current = progress.get("streak", 0)
        else:
            current = 0
        percent = min(100, int(current / g.target * 100)) if g.target > 0 else 0
        goals_data.append({"id": g.id, "goal_type": g.goal_type, "target": g.target, "current": current, "percent": percent})

    return render_template(
        "profile.html",
        user=current_user,
        total_words=len(all_w),
        total_phrases=len(get_user_phrases(uid)),
        streak=progress.get("streak", 0),
        achievements_unlocked=len(unlocked),
        achievements_total=len(ACHIEVEMENTS),
        recent_achievements=recent_ach,
        goals=goals_data,
        new_achievements=pop_new_achievements(),
    )


@app.route("/profile/upload_avatar", methods=["POST"])
@login_required
def upload_avatar():
    file = request.files.get("avatar")
    if not file:
        return redirect("/profile")
    ext = file.filename.rsplit(".", 1)[-1].lower()
    if ext not in ["jpg", "jpeg", "png", "gif"]:
        return redirect("/profile")
    filename = f"user_{current_user.id}.{ext}"
    filepath = os.path.join(app.config['AVATAR_FOLDER'], filename)
    file.save(filepath)
    current_user.avatar = filename
    db.session.commit()
    return redirect("/profile")


# ═══════════════════════════════════════════════
# СЛОВА (general)
# ═══════════════════════════════════════════════

@app.route("/add", methods=["POST"])
@login_required
def add():
    data = request.json
    eng = data["eng"].strip()
    rus = data["rus"].strip()
    section = data.get("section", "general")
    if section != "general":
        return jsonify({"status": "error", "message": "Можно добавлять только в «Общее»"})
    add_user_word(current_user.id, eng, rus, section="general")
    new_ach = check_user_achievements(current_user.id)
    if new_ach:
        session["new_achievements"] = new_ach
    return jsonify({"status": "ok"})


@app.route("/delete", methods=["POST"])
@login_required
def delete():
    data = request.json
    delete_user_word(current_user.id, data["eng"])
    return jsonify({"status": "ok"})


@app.route("/edit", methods=["POST"])
@login_required
def edit():
    data = request.json
    edit_user_word(current_user.id, data["old_eng"], data["new_eng"].strip(), data["new_rus"].strip())
    return jsonify({"status": "ok"})


# ═══════════════════════════════════════════════
# КАТЕГОРИИ
# ═══════════════════════════════════════════════

@app.route("/sections")
@login_required
def sections_page():
    uid = current_user.id
    sections_data = []
    for s in SECTIONS:
        stats = get_section_stats(uid, s["id"])
        passed_exam = SectionExam.query.filter_by(
            user_id=uid, section_id=s["id"], is_passed=True
        ).first() is not None
        sections_data.append({
            "id": s["id"], "title": s["title"], "emoji": s["emoji"],
            "count": stats["total"], "learned": stats["learned"],
            "level": s.get("level", "general"), "is_passed": passed_exam,
        })
    all_w = get_all_words(uid)
    return render_template("sections.html", sections=sections_data, total_words=len(all_w),
                           new_achievements=pop_new_achievements())


@app.route("/sections/<sid>")
@login_required
def section_page(sid):
    uid = current_user.id
    section = get_section(sid)
    if sid == "general":
        section_words = get_user_general_words(uid)
    else:
        section_words = {k: v for k, v in COMMON_WORDS.items() if v.get("section") == sid}

    learned_set = get_learned_words(uid)
    words_data = []
    for eng, data in section_words.items():
        words_data.append({"eng": eng, "rus": data["rus"], "learned": eng in learned_set})

    passed_exam = SectionExam.query.filter_by(
        user_id=uid, section_id=sid, is_passed=True
    ).first() is not None

    return render_template("section.html", section=section, words=words_data,
                           is_passed=passed_exam, new_achievements=pop_new_achievements())


@app.route("/learn_word", methods=["POST"])
@login_required
def learn_word():
    data = request.json
    word = data.get("word", "").strip()
    section = data.get("section", "general")
    if not word:
        return jsonify({"status": "error"})
    mark_learned(current_user.id, word, section)
    new_ach = check_user_achievements(current_user.id)
    if new_ach:
        session["new_achievements"] = new_ach
    return jsonify({"status": "ok"})


@app.route("/unlearn_word", methods=["POST"])
@login_required
def unlearn_word():
    data = request.json
    word = data.get("word", "").strip()
    if not word:
        return jsonify({"status": "error"})
    unmark_learned(current_user.id, word)
    return jsonify({"status": "ok"})


# ═══════════════════════════════════════════════
# ЭКЗАМЕН ПО КАТЕГОРИИ
# ═══════════════════════════════════════════════

@app.route("/exam/section/<sid>")
@login_required
def exam_section(sid):
    uid = current_user.id
    section = get_section(sid)
    if sid == "general":
        section_words = get_user_general_words(uid)
    else:
        section_words = {k: v for k, v in COMMON_WORDS.items() if v.get("section") == sid}

    if not section_words:
        return render_template("exam_section.html", empty=True, section=section)

    words_list = list(section_words.keys())
    random.shuffle(words_list)
    session["exam_section_words"] = words_list
    session["exam_section_id"] = sid
    session["exam_section_index"] = 0
    session["exam_section_errors"] = []

    return render_template("exam_section.html", empty=False, section=section, total=len(words_list))


@app.route("/exam/section/<sid>/next")
@login_required
def exam_section_next(sid):
    uid = current_user.id
    words = session.get("exam_section_words", [])
    index = session.get("exam_section_index", 0)
    if index >= len(words):
        return jsonify({"status": "end"})
    word = words[index]
    if sid == "general":
        rus = get_user_general_words(uid).get(word, {}).get("rus", "")
    else:
        rus = COMMON_WORDS.get(word, {}).get("rus", "")
    return jsonify({"status": "ok", "question_num": index + 1, "total": len(words), "word": rus})


@app.route("/exam/section/<sid>/check", methods=["POST"])
@login_required
def exam_section_check(sid):
    uid = current_user.id
    data = request.json
    answer = data.get("answer", "").strip().lower()
    words = session.get("exam_section_words", [])
    index = session.get("exam_section_index", 0)
    if index >= len(words):
        return jsonify({"status": "end"})
    word = words[index]
    is_correct = answer == word.lower()

    if not is_correct:
        errors = session.get("exam_section_errors", [])
        if sid == "general":
            rus = get_user_general_words(uid).get(word, {}).get("rus", "")
        else:
            rus = COMMON_WORDS.get(word, {}).get("rus", "")
        errors.append({"rus": rus, "correct": word, "user": answer})
        session["exam_section_errors"] = errors

    session["exam_section_index"] = index + 1
    return jsonify({
        "status": "ok", "correct": is_correct, "correct_answer": word,
        "question_num": index + 1, "total": len(words),
    })


@app.route("/exam/section/<sid>/finish", methods=["POST"])
@login_required
def exam_section_finish(sid):
    uid = current_user.id
    errors = session.get("exam_section_errors", [])
    words = session.get("exam_section_words", [])
    total = len(words)
    correct_count = total - len(errors)
    is_passed = (len(errors) == 0)

    exam = SectionExam(
        user_id=uid, section_id=sid, is_passed=is_passed,
        total_questions=total, correct_answers=correct_count,
        errors_json=json.dumps(errors, ensure_ascii=False),
    )
    db.session.add(exam)
    db.session.commit()

    new_ach = check_user_achievements(uid)
    if new_ach:
        session["new_achievements"] = new_ach

    session.pop("exam_section_words", None)
    session.pop("exam_section_id", None)
    session.pop("exam_section_index", None)
    session.pop("exam_section_errors", None)

    return jsonify({
        "status": "ok", "is_passed": is_passed, "total": total,
        "correct": correct_count, "errors": errors,
        "new_achievements": [get_achievement(c) for c in new_ach if get_achievement(c)],
    })


# ═══════════════════════════════════════════════
# ТРЕНИРОВКА СЛОВ
# ═══════════════════════════════════════════════

@app.route("/train")
@login_required
def train():
    uid = current_user.id
    section_id = request.args.get("section", "")
    reverse = request.args.get("reverse", "0") == "1"
    reset = request.args.get("reset", "0") == "1"
    weak_mode = request.args.get("weak", "0") == "1"
    mode = request.args.get("mode", "normal")  # normal / listening

    if reset or "train_correct" not in session:
        session["train_correct"] = 0
        session["train_wrong"] = 0

    if weak_mode:
        progress = get_user_progress(uid)
        weak_set = set(progress.get("weak_words", {}).keys())
        all_w = get_all_words(uid)
        filtered = {k: v for k, v in all_w.items() if k in weak_set}
    elif section_id == "general":
        filtered = get_user_general_words(uid)
    elif section_id:
        filtered = {k: v for k, v in COMMON_WORDS.items() if v.get("section") == section_id}
    else:
        filtered = get_all_words(uid)

    learned_set = get_learned_words(uid)
    filtered = {k: v for k, v in filtered.items() if k not in learned_set}

    last_word = session.get("last_train_word")
    if len(filtered) > 1 and last_word in filtered:
        filtered = {k: v for k, v in filtered.items() if k != last_word}

    if not filtered:
        return render_template("train.html", word=None, empty=True, reverse=reverse, section=section_id,
                               correct_count=session.get("train_correct", 0),
                               wrong_count=session.get("train_wrong", 0),
                               weak_mode=weak_mode, mode=mode)

    eng = random.choice(list(filtered.keys()))
    session["current_word"] = eng
    session["last_train_word"] = eng
    session["train_reverse"] = reverse
    session["train_section"] = section_id
    session["train_mode"] = mode

    if mode == "listening":
        display = "🎧"
    elif reverse:
        display = filtered[eng]["rus"]
    else:
        display = eng

    return render_template("train.html", word=display, empty=False, reverse=reverse, section=section_id,
                           correct_count=session.get("train_correct", 0),
                           wrong_count=session.get("train_wrong", 0),
                           weak_mode=weak_mode, mode=mode)


@app.route("/check", methods=["POST"])
@login_required
def check():
    data = request.json
    uid = current_user.id
    all_w = get_all_words(uid)
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_word")
    reverse = session.get("train_reverse", False)
    mode = session.get("train_mode", "normal")

    if not eng or eng not in all_w:
        return jsonify({"status": "error"})

    if mode == "listening":
        correct_answer = eng.lower()
    elif reverse:
        correct_answer = eng.lower()
    else:
        correct_answer = all_w[eng]["rus"].strip().lower()

    if user_answer == correct_answer:
        session["train_correct"] = session.get("train_correct", 0) + 1
        record_training(True, eng)
        new_ach = check_user_achievements(uid)
        if new_ach:
            session["new_achievements"] = new_ach
        return jsonify({
            "status": "correct",
            "correct_answer": eng if (reverse or mode == "listening") else all_w[eng]["rus"],
            "correct_count": session["train_correct"],
            "wrong_count": session.get("train_wrong", 0),
        })
    else:
        session["train_wrong"] = session.get("train_wrong", 0) + 1
        record_training(False, eng)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng if (reverse or mode == "listening") else all_w[eng]["rus"],
            "correct_count": session.get("train_correct", 0),
            "wrong_count": session["train_wrong"],
        })


# ═══════════════════════════════════════════════
# ФРАЗЫ
# ═══════════════════════════════════════════════

@app.route("/phrases")
@login_required
def phrases_page():
    return render_template("phrases.html", phrases=get_user_phrases(current_user.id),
                           new_achievements=pop_new_achievements())


@app.route("/phrases/add", methods=["POST"])
@login_required
def phrases_add():
    data = request.json
    add_user_phrase(current_user.id, data["eng"], data["rus"])
    new_ach = check_user_achievements(current_user.id)
    if new_ach:
        session["new_achievements"] = new_ach
    return jsonify({"status": "ok"})


@app.route("/phrases/delete", methods=["POST"])
@login_required
def phrases_delete():
    data = request.json
    delete_user_phrase(current_user.id, data["eng"])
    return jsonify({"status": "ok"})


@app.route("/phrases/edit", methods=["POST"])
@login_required
def phrases_edit():
    data = request.json
    edit_user_phrase(current_user.id, data["old_eng"], data["new_eng"], data["new_rus"])
    return jsonify({"status": "ok"})


@app.route("/phrases/train")
@login_required
def phrases_train():
    p = get_user_phrases(current_user.id)
    reverse = request.args.get("reverse", "0") == "1"
    reset = request.args.get("reset", "0") == "1"

    if reset or "phrases_correct" not in session:
        session["phrases_correct"] = 0
        session["phrases_wrong"] = 0

    if not p:
        return render_template("train_phrases.html", phrase=None, empty=True, reverse=reverse,
                               correct_count=session.get("phrases_correct", 0),
                               wrong_count=session.get("phrases_wrong", 0))

    eng = random.choice(list(p.keys()))
    session["current_phrase"] = eng
    session["phrase_reverse"] = reverse
    display = p[eng] if reverse else eng
    return render_template("train_phrases.html", phrase=display, empty=False, reverse=reverse,
                           correct_count=session.get("phrases_correct", 0),
                           wrong_count=session.get("phrases_wrong", 0))


@app.route("/phrases/check", methods=["POST"])
@login_required
def phrases_check():
    data = request.json
    p = get_user_phrases(current_user.id)
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_phrase")
    reverse = session.get("phrase_reverse", False)
    if not eng or eng not in p:
        return jsonify({"status": "error"})
    correct_answer = eng.lower() if reverse else p[eng].strip().lower()

    if user_answer == correct_answer:
        session["phrases_correct"] = session.get("phrases_correct", 0) + 1
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": eng if reverse else p[eng],
            "correct_count": session["phrases_correct"],
            "wrong_count": session.get("phrases_wrong", 0),
        })
    else:
        session["phrases_wrong"] = session.get("phrases_wrong", 0) + 1
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng if reverse else p[eng],
            "correct_count": session.get("phrases_correct", 0),
            "wrong_count": session["phrases_wrong"],
        })


# ═══════════════════════════════════════════════
# ПРОГРЕСС
# ═══════════════════════════════════════════════

@app.route("/progress")
@login_required
def progress_page():
    uid = current_user.id
    progress = get_user_progress(uid)
    all_w = get_all_words(uid)
    total_correct = sum(d["correct"] for d in progress["history"])
    total_wrong = sum(d["wrong"] for d in progress["history"])
    total_answers = total_correct + total_wrong
    accuracy = round(total_correct / total_answers * 100) if total_answers > 0 else 0

    last_7 = []
    for i in range(6, -1, -1):
        day = str(date.today() - timedelta(days=i))
        day_data = next((d for d in progress["history"] if d["date"] == day), None)
        last_7.append({
            "date": day,
            "label": day[8:10] + "." + day[5:7],
            "correct": day_data["correct"] if day_data else 0,
            "wrong": day_data["wrong"] if day_data else 0,
        })

    max_day = max((d["correct"] + d["wrong"] for d in last_7), default=1)
    if max_day == 0:
        max_day = 1

    today = date.today()
    first_day = today.replace(day=1)
    if today.month == 12:
        next_month = today.replace(year=today.year + 1, month=1, day=1)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
    days_in_month = (next_month - first_day).days
    first_weekday = first_day.weekday()

    calendar_days = []
    for _ in range(first_weekday):
        calendar_days.append({"empty": True})
    for day_num in range(1, days_in_month + 1):
        day_str = str(today.replace(day=day_num))
        trained = any(d["date"] == day_str and (d["correct"] + d["wrong"]) > 0 for d in progress["history"])
        is_today = (day_num == today.day)
        calendar_days.append({"empty": False, "day": day_num, "trained": trained, "today": is_today})

    weak_words = progress.get("weak_words", {})
    weak_sorted = sorted(weak_words.items(), key=lambda x: x[1], reverse=True)[:10]
    weak_list = []
    for w, count in weak_sorted:
        if w in all_w:
            weak_list.append({"word": w, "rus": all_w[w]["rus"], "count": count})

    return render_template(
        "progress.html",
        total_words=len(all_w),
        total_phrases=len(get_user_phrases(uid)),
        total_correct=total_correct,
        total_wrong=total_wrong,
        accuracy=accuracy,
        streak=progress["streak"],
        last_7=last_7,
        max_day=max_day,
        calendar_days=calendar_days,
        weak_words=weak_list,
        month_name=today.strftime("%B %Y"),
        new_achievements=pop_new_achievements(),
    )


# ═══════════════════════════════════════════════
# ДОСТИЖЕНИЯ
# ═══════════════════════════════════════════════

@app.route("/achievements")
@login_required
def achievements_page():
    uid = current_user.id
    check_user_achievements(uid)

    unlocked = get_unlocked_codes(uid)
    categories = {}
    for a in ACHIEVEMENTS:
        cat = a["category"]
        categories.setdefault(cat, []).append({**a, "unlocked": a["code"] in unlocked})

    return render_template(
        "achievements.html",
        categories=categories,
        total=len(ACHIEVEMENTS),
        unlocked_count=len(unlocked),
        new_achievements=pop_new_achievements(),
    )


# ═══════════════════════════════════════════════
# ЦЕЛИ
# ═══════════════════════════════════════════════

@app.route("/goals")
@login_required
def goals_page():
    uid = current_user.id
    goals = Goal.query.filter_by(user_id=uid).order_by(Goal.is_completed, Goal.created_at.desc()).all()

    progress = get_user_progress(uid)
    all_w = get_all_words(uid)

    goals_data = []
    for g in goals:
        if g.goal_type == "words":
            current = len(all_w)
        elif g.goal_type == "streak":
            current = progress.get("streak", 0)
        else:
            current = 0

        percent = min(100, int(current / g.target * 100)) if g.target > 0 else 0
        if current >= g.target and not g.is_completed:
            g.is_completed = True
            g.completed_at = datetime.utcnow()
            db.session.commit()

        goals_data.append({
            "id": g.id, "goal_type": g.goal_type, "target": g.target,
            "deadline": g.deadline, "current": current,
            "percent": percent, "is_completed": g.is_completed,
        })

    return render_template("goals.html", goals=goals_data,
                           new_achievements=pop_new_achievements())


@app.route("/goals/new", methods=["POST"])
@login_required
def goal_new():
    uid = current_user.id
    data = request.json
    goal_type = data.get("goal_type", "").strip()
    target = data.get("target", 0)
    deadline_str = data.get("deadline", "").strip()

    if goal_type not in ("words", "streak"):
        return jsonify({"status": "error", "message": "Неверный тип"})
    try:
        target = int(target)
        if target <= 0 or target > 100000:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"status": "error", "message": "Неверное число"})

    deadline = None
    if deadline_str:
        try:
            deadline = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        except ValueError:
            return jsonify({"status": "error", "message": "Неверная дата"})

    db.session.add(Goal(user_id=uid, goal_type=goal_type, target=target, deadline=deadline))
    db.session.commit()
    return jsonify({"status": "ok"})


@app.route("/goals/delete", methods=["POST"])
@login_required
def goal_delete():
    uid = current_user.id
    data = request.json
    gid = data.get("id")
    goal = Goal.query.filter_by(id=gid, user_id=uid).first()
    if goal:
        db.session.delete(goal)
        db.session.commit()
    return jsonify({"status": "ok"})


# ═══════════════════════════════════════════════
# ТОПИКИ
# ═══════════════════════════════════════════════

@app.route("/topics")
@login_required
def topics_page():
    uid = current_user.id
    user_topics = get_user_topics(uid)
    all_topics = []
    for t in FIXED_TOPICS:
        data = user_topics.get(t["id"], {})
        all_topics.append({
            "id": t["id"], "title": t["title"], "emoji": t["emoji"],
            "text": data.get("text", ""), "done": data.get("done", False),
            "word_count": len(data.get("text", "").split()) if data.get("text") else 0,
        })
    for tid, data in user_topics.items():
        if tid.startswith("custom_"):
            all_topics.append({
                "id": tid, "title": data.get("title", "Своя тема"), "emoji": "📝",
                "text": data.get("text", ""), "done": data.get("done", False),
                "word_count": len(data.get("text", "").split()) if data.get("text") else 0,
            })
    return render_template("topics.html", topics=all_topics,
                           new_achievements=pop_new_achievements())


@app.route("/topics/<tid>")
@login_required
def topic_page(tid):
    uid = current_user.id
    user_topics = get_user_topics(uid)
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    if not topic_info:
        if tid in user_topics:
            topic_info = {"id": tid, "title": user_topics[tid].get("title", "Своя тема"), "emoji": "📝", "helper": []}
        else:
            return "Тема не найдена", 404
    data = user_topics.get(tid, {"text": "", "done": False})
    return render_template("topic.html", topic=topic_info, text=data.get("text", ""), done=data.get("done", False))


@app.route("/topics/<tid>/save", methods=["POST"])
@login_required
def topic_save(tid):
    uid = current_user.id
    data = request.json
    text = data["text"].strip()
    if len(text.split()) < 50:
        return jsonify({"status": "error", "message": "Минимум 50 слов"})
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    existing = get_user_topics(uid).get(tid, {})
    title = topic_info["title"] if topic_info else existing.get("title", "Своя тема")
    save_user_topic(uid, tid, title, text, True)

    new_ach = check_user_achievements(uid)
    if new_ach:
        session["new_achievements"] = new_ach

    return jsonify({"status": "ok"})


@app.route("/topics/new", methods=["GET", "POST"])
@login_required
def topic_new():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            return redirect("/topics/new")
        tid = "custom_" + str(int(time.time()))
        create_user_topic(current_user.id, tid, title)
        return redirect(f"/topics/{tid}")
    return render_template("topic_new.html")


@app.route("/topics/<tid>/delete", methods=["POST"])
@login_required
def topic_delete(tid):
    if tid.startswith("custom_"):
        delete_user_topic(current_user.id, tid)
    return jsonify({"status": "ok"})


# ═══════════════════════════════════════════════
# ЭКЗАМЕН-ТЕКСТ
# ═══════════════════════════════════════════════

@app.route("/exam")
@login_required
def exam_page():
    uid = current_user.id
    all_topics = list(FIXED_TOPICS)
    for tid, data in get_user_topics(uid).items():
        if tid.startswith("custom_"):
            all_topics.append({"id": tid, "title": data.get("title", "Своя тема"), "emoji": "📝", "helper": []})
    if not all_topics:
        return render_template("exam.html", topic=None, empty=True)
    topic = random.choice(all_topics)
    session["exam_topic"] = topic["id"]
    session["exam_start"] = str(date.today())
    return render_template("exam.html", topic=topic, empty=False)


@app.route("/exam/save", methods=["POST"])
@login_required
def exam_save():
    uid = current_user.id
    data = request.json
    text = data["text"].strip()
    tid = session.get("exam_topic")
    if not tid:
        return jsonify({"status": "error"})
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    title = topic_info["title"] if topic_info else get_user_topics(uid).get(tid, {}).get("title", "Своя тема")
    exam_id = str(int(time.time()))
    save_user_exam(uid, exam_id, tid, title, text, len(text.split()))

    if unlock(uid, "exam_text_1"):
        session["new_achievements"] = ["exam_text_1"]

    return jsonify({"status": "ok", "exam_id": exam_id})


@app.route("/exam/history")
@login_required
def exam_history():
    exams_list = []
    for eid, data in get_user_exams(current_user.id).items():
        exams_list.append({"id": eid, "title": data["title"], "date": data["date"], "word_count": data["word_count"]})
    return render_template("exam_history.html", exams=exams_list)


# ═══════════════════════════════════════════════
# ПЕРЕВОДЧИК
# ═══════════════════════════════════════════════

@app.route("/translator")
@login_required
def translator_page():
    return render_template("translator.html")


@app.route("/translate", methods=["POST"])
@login_required
def translate():
    data = request.json
    text = data.get("text", "").strip()
    direction = data.get("direction", "ru-en")
    if not text:
        return jsonify({"status": "error", "message": "Пустой текст"})
    try:
        if direction == "ru-en":
            translated = MyMemoryTranslator(source='ru-RU', target='en-GB').translate(text)
        else:
            translated = MyMemoryTranslator(source='en-GB', target='ru-RU').translate(text)
        return jsonify({"status": "ok", "translation": translated})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})


@app.route("/faq")
def faq_page():
    return render_template("faq.html")


# ═══════════════════════════════════════════════
# УЧЁБА
# ═══════════════════════════════════════════════

@app.route("/study")
@login_required
def study_page():
    return render_template("study.html")


@app.route("/study/irregular")
@login_required
def irregular_page():
    return render_template("irregular.html", verbs=IRREGULAR_VERBS)


@app.route("/study/phrasal")
@login_required
def phrasal_page():
    return render_template("phrasal.html", verbs=PHRASAL_VERBS)


@app.route("/study/idioms")
@login_required
def idioms_page():
    return render_template("idioms.html", idioms=IDIOMS)


@app.route("/study/irregular/train")
@login_required
def irregular_train():
    mode = request.args.get("mode", "past")
    session["irr_mode"] = mode
    session["irr_correct"] = 0
    session["irr_wrong"] = 0
    session["irr_used"] = []
    return render_template("irregular_train.html", empty=False, mode=mode)


@app.route("/study/irregular/next")
@login_required
def irregular_next():
    mode = session.get("irr_mode", "past")
    used = session.get("irr_used", [])
    available = [v for v in IRREGULAR_VERBS if v["base"] not in used]
    if not available:
        return jsonify({"status": "end"})
    verb = random.choice(available)
    session["irr_used"] = used + [verb["base"]]
    session["irr_current"] = verb["base"]

    if mode == "past":
        return jsonify({"status": "ok", "question": verb["base"], "question_label": "Base → Past", "hint": "Какая форма Past?"})
    elif mode == "pp":
        return jsonify({"status": "ok", "question": verb["base"], "question_label": "Base → Past Participle", "hint": "Какая форма Past Participle?"})
    else:
        form = random.choice(["past", "pp"])
        session["irr_mixed_form"] = form
        if form == "past":
            return jsonify({"status": "ok", "question": verb["base"], "question_label": "Base → Past", "hint": "Какая форма Past?"})
        else:
            return jsonify({"status": "ok", "question": verb["pp"], "question_label": "Past Participle → Base", "hint": "Какой это глагол?"})


@app.route("/study/irregular/check", methods=["POST"])
@login_required
def irregular_check():
    data = request.json
    answer = data.get("answer", "").strip().lower()
    base = session.get("irr_current", "")
    mode = session.get("irr_mode", "past")
    verb = next((v for v in IRREGULAR_VERBS if v["base"] == base), None)
    if not verb:
        return jsonify({"status": "error"})

    if mode == "past":
        correct, correct_display = verb["past"].lower(), verb["past"]
    elif mode == "pp":
        correct, correct_display = verb["pp"].lower(), verb["pp"]
    else:
        form = session.get("irr_mixed_form", "past")
        if form == "past":
            correct, correct_display = verb["past"].lower(), verb["past"]
        else:
            correct, correct_display = verb["base"].lower(), verb["base"]

    is_correct = answer == correct
    if is_correct:
        session["irr_correct"] = session.get("irr_correct", 0) + 1
    else:
        session["irr_wrong"] = session.get("irr_wrong", 0) + 1

    return jsonify({
        "status": "ok", "correct": is_correct, "correct_answer": correct_display,
        "score": session.get("irr_correct", 0), "wrong": session.get("irr_wrong", 0),
    })


# ═══════════════════════════════════════════════
# ИГРЫ
# ═══════════════════════════════════════════════

@app.route("/games")
@login_required
def games_page():
    return render_template("games.html")


# ─── АУДИО-КВИЗ ───

@app.route("/games/listening")
@login_required
def listening_page():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 2 <= len(w) <= 20 and " " not in w]
    if len(available) < 4:
        return render_template("games_listening.html", empty=True)
    total = min(10, len(available))
    session["listening_score"] = 0
    session["listening_question"] = 0
    session["listening_total"] = total
    session["listening_used"] = []
    session["listening_errors"] = []
    return render_template("games_listening.html", empty=False)


@app.route("/games/listening/question")
@login_required
def listening_question():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 2 <= len(w) <= 20 and " " not in w and w not in session.get("listening_used", [])]
    if not available or session.get("listening_question", 0) >= session.get("listening_total", 10):
        return jsonify({"status": "end"})

    word = random.choice(available)
    session["listening_used"] = session.get("listening_used", []) + [word]
    session["listening_current"] = word
    correct = all_w[word]["rus"]
    others = [w for w in all_w.keys() if w != word and all_w[w]["rus"] != correct]
    wrong_options = random.sample(others, min(3, len(others)))
    wrong_answers = [all_w[w]["rus"] for w in wrong_options]
    options = [correct] + wrong_answers
    random.shuffle(options)

    question_num = session.get("listening_question", 0) + 1
    session["listening_question"] = question_num
    return jsonify({
        "status": "ok",
        "word": word,
        "options": options,
        "correct": correct,
        "question_num": question_num,
        "total": session.get("listening_total", 10),
    })


@app.route("/games/listening/answer", methods=["POST"])
@login_required
def listening_answer():
    all_w = get_all_words(current_user.id)
    data = request.json
    answer = data.get("answer", "").strip()
    word = session.get("listening_current", "")
    if not word or word not in all_w:
        return jsonify({"status": "error"})
    correct = all_w[word]["rus"]
    is_correct = (answer == correct)
    if is_correct:
        session["listening_score"] = session.get("listening_score", 0) + 1
    else:
        errors = session.get("listening_errors", [])
        errors.append({"word": word, "correct": correct, "chosen": answer})
        session["listening_errors"] = errors
    return jsonify({
        "status": "ok",
        "correct": is_correct,
        "correct_answer": correct,
        "score": session.get("listening_score", 0),
    })


@app.route("/games/listening/result")
@login_required
def listening_result():
    score = session.get("listening_score", 0)
    total = session.get("listening_total", 10)
    if score == total and total >= 10:
        unlock(current_user.id, "game_listening_10")
    return jsonify({
        "score": score,
        "total": total,
        "errors": session.get("listening_errors", []),
    })


# ─── ВИСЕЛИЦА ───

@app.route("/games/hangman")
@login_required
def hangman_page():
    uid = current_user.id
    all_w = get_all_words(uid)
    available = [w for w in all_w.keys() if 4 <= len(w) <= 12 and " " not in w]
    if not available:
        return render_template("hangman.html", empty=True)
    word = random.choice(available).lower()
    section = get_section(all_w[word]["section"])
    session["hangman_word"] = word
    session["hangman_guessed"] = []
    session["hangman_errors"] = 0
    display = " ".join(["_" for _ in word])
    return render_template("hangman.html", empty=False, display=display, errors=0,
                           max_errors=6, guessed=[], word_length=len(word), section=section)


@app.route("/games/hangman/guess", methods=["POST"])
@login_required
def hangman_guess():
    data = request.json
    letter = data.get("letter", "").strip().lower()
    if len(letter) != 1 or not letter.isalpha() or not letter.isascii():
        return jsonify({"status": "error", "message": "Только одна английская буква"})

    word = session.get("hangman_word", "")
    guessed = session.get("hangman_guessed", [])
    errors = session.get("hangman_errors", 0)
    if not word:
        return jsonify({"status": "error", "message": "Игра не найдена"})

    if letter in guessed:
        return jsonify({
            "status": "already",
            "display": " ".join([c if c in guessed else "_" for c in word]),
            "errors": errors, "guessed": guessed,
            "message": "Эту букву уже называл",
        })

    guessed.append(letter)
    if letter not in word:
        errors += 1
    session["hangman_guessed"] = guessed
    session["hangman_errors"] = errors
    display = " ".join([c if c in guessed else "_" for c in word])

    if all(c in guessed for c in word):
        unlock(current_user.id, "game_hangman_win")
        return jsonify({"status": "win", "display": display, "word": word, "errors": errors,
                        "guessed": guessed, "message": "🎉 Ты угадал! Слово: " + word})
    if errors >= 6:
        return jsonify({"status": "lose", "display": display, "word": word, "errors": errors,
                        "guessed": guessed, "message": "💀 Ты проиграл. Слово было: " + word})
    return jsonify({"status": "ok", "display": display, "errors": errors, "guessed": guessed})


# ─── КВИЗ ───

@app.route("/games/quiz")
@login_required
def quiz_page():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 4 <= len(w) <= 12 and " " not in w]
    if len(available) < 4:
        return render_template("quiz.html", empty=True)
    total = min(10, len(available))
    session["quiz_score"] = 0
    session["quiz_question"] = 0
    session["quiz_total"] = total
    session["quiz_used"] = []
    session["quiz_errors"] = []
    return render_template("quiz.html", empty=False)


@app.route("/games/quiz/question")
@login_required
def quiz_question():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 4 <= len(w) <= 12 and " " not in w and w not in session.get("quiz_used", [])]
    if not available or session.get("quiz_question", 0) >= session.get("quiz_total", 10):
        return jsonify({"status": "end"})

    word = random.choice(available)
    session["quiz_used"] = session.get("quiz_used", []) + [word]
    session["quiz_current"] = word
    correct = all_w[word]["rus"]
    others = [w for w in all_w.keys() if w != word and all_w[w]["rus"] != correct]
    wrong_options = random.sample(others, min(3, len(others)))
    wrong_answers = [all_w[w]["rus"] for w in wrong_options]
    options = [correct] + wrong_answers
    random.shuffle(options)

    question_num = session.get("quiz_question", 0) + 1
    session["quiz_question"] = question_num
    return jsonify({"status": "ok", "word": word, "options": options, "correct": correct,
                    "question_num": question_num, "total": session.get("quiz_total", 10)})


@app.route("/games/quiz/answer", methods=["POST"])
@login_required
def quiz_answer():
    all_w = get_all_words(current_user.id)
    data = request.json
    answer = data.get("answer", "").strip()
    word = session.get("quiz_current", "")
    if not word or word not in all_w:
        return jsonify({"status": "error"})
    correct = all_w[word]["rus"]
    is_correct = (answer == correct)
    if is_correct:
        session["quiz_score"] = session.get("quiz_score", 0) + 1
    else:
        errors = session.get("quiz_errors", [])
        errors.append({"word": word, "correct": correct, "chosen": answer})
        session["quiz_errors"] = errors
    return jsonify({"status": "ok", "correct": is_correct, "correct_answer": correct,
                    "score": session.get("quiz_score", 0)})


@app.route("/games/quiz/result")
@login_required
def quiz_result():
    score = session.get("quiz_score", 0)
    total = session.get("quiz_total", 10)
    if score == total and total >= 10:
        unlock(current_user.id, "game_quiz_10")
    return jsonify({
        "score": score, "total": total,
        "errors": session.get("quiz_errors", []),
    })


# ─── СКОРОСТНОЙ ───

@app.route("/games/speed")
@login_required
def speed_page():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 2 <= len(w) <= 15]
    if len(available) < 5:
        return render_template("speed.html", empty=True)
    return render_template("speed.html", empty=False)


@app.route("/games/speed/start")
@login_required
def speed_start():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 2 <= len(w) <= 15]
    if len(available) < 5:
        return jsonify({"status": "error"})
    chosen = random.sample(available, min(10, len(available)))
    session["speed_words"] = chosen
    session["speed_index"] = 0
    session["speed_score"] = 0
    session["speed_start"] = time.time()
    return jsonify({"status": "ok", "total": len(chosen)})


@app.route("/games/speed/next")
@login_required
def speed_next():
    speed_words = session.get("speed_words", [])
    index = session.get("speed_index", 0)
    if index >= len(speed_words):
        return jsonify({"status": "end"})
    return jsonify({"status": "ok", "word": speed_words[index], "index": index + 1, "total": len(speed_words)})


@app.route("/games/speed/check", methods=["POST"])
@login_required
def speed_check():
    all_w = get_all_words(current_user.id)
    data = request.json
    answer = data.get("answer", "").strip().lower()
    speed_words = session.get("speed_words", [])
    index = session.get("speed_index", 0)
    if index >= len(speed_words):
        return jsonify({"status": "error"})
    word = speed_words[index]
    correct = all_w[word]["rus"].strip().lower()
    is_correct = (answer == correct)
    if is_correct:
        session["speed_score"] = session.get("speed_score", 0) + 1
    session["speed_index"] = index + 1
    return jsonify({"status": "ok", "correct": is_correct, "correct_answer": all_w[word]["rus"],
                    "score": session.get("speed_score", 0), "index": index + 1, "total": len(speed_words)})


@app.route("/games/speed/result")
@login_required
def speed_result():
    score = session.get("speed_score", 0)
    total = len(session.get("speed_words", []))
    if score == total and total >= 10:
        unlock(current_user.id, "game_speed_10")
    return jsonify({"score": score, "total": total})


# ═══════════════════════════════════════════════
# УТИЛИТЫ
# ═══════════════════════════════════════════════

@app.route("/utils")
@login_required
def utils_page():
    return render_template("utils.html")


@app.route("/export/words")
@login_required
def export_words():
    uid = current_user.id
    all_w = get_all_words(uid)
    text = "МОИ СЛОВА\n\n"
    for eng, data in all_w.items():
        section = get_section(data["section"])
        text += f"{eng} - {data['rus']} ({section['title']})\n"
    return Response(text, mimetype="text/plain", headers={"Content-Disposition": "attachment; filename=my_words.txt"})


@app.route("/export/phrases")
@login_required
def export_phrases():
    text = "МОИ ФРАЗЫ\n\n"
    for eng, rus in get_user_phrases(current_user.id).items():
        text += f"{eng} - {rus}\n"
    return Response(text, mimetype="text/plain", headers={"Content-Disposition": "attachment; filename=my_phrases.txt"})


@app.route("/export/section/<sid>")
@login_required
def export_section(sid):
    uid = current_user.id
    section = get_section(sid)
    if sid == "general":
        words_to_export = get_user_general_words(uid)
    else:
        words_to_export = {k: v for k, v in COMMON_WORDS.items() if v.get("section") == sid}
    text = f"КАТЕГОРИЯ: {section['title'].upper()}\n\n"
    for eng, data in words_to_export.items():
        text += f"{eng} - {data['rus']}\n"
    return Response(text, mimetype="text/plain", headers={"Content-Disposition": f"attachment; filename={sid}.txt"})


@app.route("/export/topics")
@login_required
def export_topics():
    text = "МОИ ТОПИКИ\n\n"
    for tid, data in get_user_topics(current_user.id).items():
        if data.get("done"):
            text += f"=== {data.get('title', 'Без названия')} ===\n"
            text += data.get("text", "") + "\n\n"
    return Response(text, mimetype="text/plain", headers={"Content-Disposition": "attachment; filename=my_topics.txt"})


# ═══════════════════════════════════════════════
# АВТОРИЗАЦИЯ
# ═══════════════════════════════════════════════

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not email or not username or not password:
            return render_template("register.html", error="Заполни все поля")
        if User.query.filter_by(email=email).first():
            return render_template("register.html", error="Этот email уже занят")

        code = str(random.randint(100000, 999999))
        db.session.add(EmailCode(email=email, code=code))
        db.session.commit()

        try:
            send_verification_code(email, code)
        except Exception as e:
            return render_template("register.html", error=f"Ошибка отправки: {e}")

        session["reg_email"] = email
        session["reg_username"] = username
        session["reg_password"] = password
        return redirect("/verify")
    return render_template("register.html")


@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        user_code = request.form.get("code", "").strip()
        email = session.get("reg_email")
        if not email:
            return redirect("/register")
        record = EmailCode.query.filter_by(email=email).order_by(EmailCode.id.desc()).first()
        if not record or record.code != user_code:
            return render_template("verify.html", error="Неверный код")
        db.session.delete(record)
        hashed = generate_password_hash(session.get("reg_password"))
        user = User(email=email, username=session.get("reg_username"), password=hashed, is_verified=True)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        session.pop("reg_email", None)
        session.pop("reg_username", None)
        session.pop("reg_password", None)
        return redirect("/")
    return render_template("verify.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return render_template("login.html", error="Неверный email или пароль")
        login_user(user)
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
