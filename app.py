from flask import Flask, render_template, request, jsonify, session, redirect
import json
import random
import os
from datetime import date, timedelta

app = Flask(__name__)
app.secret_key = "johnny_english_secret_key_change_me"

WORDS_FILE = "/data/words.json"
PHRASES_FILE = "/data/phrases.json"
PROGRESS_FILE = "/data/progress.json"
TOPICS_FILE = "/data/topics.json"

# ─── РАЗДЕЛЫ ───

SECTIONS = [
    {"id": "food", "title": "Еда", "emoji": "🍔"},
    {"id": "sport", "title": "Спорт", "emoji": "⚽"},
    {"id": "work", "title": "Работа", "emoji": "💼"},
    {"id": "travel", "title": "Путешествия", "emoji": "✈️"},
    {"id": "family", "title": "Семья", "emoji": "👨‍👩‍👧"},
    {"id": "general", "title": "Общее", "emoji": "📦"},
]

def get_section(sid):
    return next((s for s in SECTIONS if s["id"] == sid), SECTIONS[-1])

# ─── ЗАГРУЗКА ДАННЫХ ───

# Миграция: если /data/words.json пустой или не существует — берём из репозитория
DATA_EMPTY = False
try:
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        raw_words = json.load(f)
    if not raw_words:
        DATA_EMPTY = True
except:
    DATA_EMPTY = True

if DATA_EMPTY:
    # Читаем из репозитория и сохраняем в /data/
    try:
        with open("words.json", "r", encoding="utf-8") as f:
            raw_words = json.load(f)
        # Сразу сохраняем в /data/
        with open(WORDS_FILE, "w", encoding="utf-8") as f:
            json.dump(raw_words, f, ensure_ascii=False, indent=2)
    except:
        raw_words = {"hello": "привет", "go": "идти", "cat": "кот"}

# Миграция: превращаем старый формат в новый
words = {}
for k, v in raw_words.items():
    if isinstance(v, dict):
        # Новый формат — уже с section
        section = v.get("section", "general")
        if section not in [s["id"] for s in SECTIONS]:
            section = "general"
        words[k] = {"rus": v.get("rus", ""), "section": section}
    else:
        # Старый формат — просто строка
        words[k] = {"rus": v, "section": "general"}

def save_words():
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

try:
    with open(PHRASES_FILE, "r", encoding="utf-8") as f:
        phrases = json.load(f)
except:
    phrases = {"How are you?": "Как дела?", "Thank you": "Спасибо"}

def save_phrases():
    with open(PHRASES_FILE, "w", encoding="utf-8") as f:
        json.dump(phrases, f, ensure_ascii=False, indent=2)

try:
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        progress = json.load(f)
except:
    progress = {"history": [], "streak": 0, "last_day": ""}

def save_progress():
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

try:
    with open(TOPICS_FILE, "r", encoding="utf-8") as f:
        topics = json.load(f)
except:
    topics = {}

def save_topics():
    with open(TOPICS_FILE, "w", encoding="utf-8") as f:
        json.dump(topics, f, ensure_ascii=False, indent=2)

def record_training(correct: bool):
    today = str(date.today())
    if progress["last_day"] != today:
        yesterday = str(date.today() - timedelta(days=1))
        if progress["last_day"] == yesterday:
            progress["streak"] += 1
        else:
            progress["streak"] = 1
        progress["last_day"] = today

    if not progress["history"] or progress["history"][-1]["date"] != today:
        progress["history"].append({"date": today, "correct": 0, "wrong": 0})

    if correct:
        progress["history"][-1]["correct"] += 1
    else:
        progress["history"][-1]["wrong"] += 1

    save_progress()

# ─── СЛОВА ───

@app.route("/")
def index():
    total_words = len(words)
    total_phrases = len(phrases)
    total_topics_done = sum(1 for t in topics.values() if t.get("done"))
    total_topics = len(FIXED_TOPICS) + sum(1 for t in topics.keys() if t.startswith("custom_"))
    streak = progress.get("streak", 0)
    return render_template(
        "index.html",
        total_words=total_words,
        total_phrases=total_phrases,
        total_topics_done=total_topics_done,
        total_topics=total_topics,
        streak=streak
    )

@app.route("/words")
def words_page():
    return render_template("words.html", words=words, sections=SECTIONS)

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    eng = data["eng"].strip()
    rus = data["rus"].strip()
    section = data.get("section", "general")
    if section not in [s["id"] for s in SECTIONS]:
        section = "general"
    words[eng] = {"rus": rus, "section": section}
    save_words()
    return jsonify({"status": "ok"})

@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    eng = data["eng"]
    if eng in words:
        del words[eng]
        save_words()
    return jsonify({"status": "ok"})

@app.route("/edit", methods=["POST"])
def edit():
    data = request.json
    old_eng = data["old_eng"]
    new_eng = data["new_eng"].strip()
    new_rus = data["new_rus"].strip()
    section = data.get("section", "general")
    if old_eng in words:
        del words[old_eng]
        words[new_eng] = {"rus": new_rus, "section": section}
        save_words()
    return jsonify({"status": "ok"})

# ─── РАЗДЕЛЫ ───

@app.route("/sections")
def sections_page():
    sections_data = []
    for s in SECTIONS:
        section_words = {k: v for k, v in words.items() if v["section"] == s["id"]}
        sections_data.append({
            "id": s["id"],
            "title": s["title"],
            "emoji": s["emoji"],
            "count": len(section_words)
        })
    total_words = len(words)
    return render_template("sections.html", sections=sections_data, total_words=total_words)

@app.route("/sections/<sid>")
def section_page(sid):
    section = get_section(sid)
    section_words = {k: v for k, v in words.items() if v["section"] == sid}
    return render_template("section.html", section=section, words=section_words)

# ─── ТРЕНИРОВКА ───

@app.route("/train")
def train():
    section_id = request.args.get("section", "")
    if section_id:
        filtered = {k: v for k, v in words.items() if v["section"] == section_id}
        if not filtered:
            return render_template("train.html", word=None, empty=True)
        eng = random.choice(list(filtered.keys()))
    else:
        if not words:
            return render_template("train.html", word=None, empty=True)
        eng = random.choice(list(words.keys()))
    session["current_word"] = eng
    return render_template("train.html", word=eng, empty=False)

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_word")
    if not eng or eng not in words:
        return jsonify({"status": "error"})
    correct_answer = words[eng]["rus"].strip().lower()
    if user_answer == correct_answer:
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": words[eng]["rus"],
            "correct_count": session.get("correct", 0) + 1,
            "wrong_count": session.get("wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": words[eng]["rus"],
            "correct_count": session.get("correct", 0),
            "wrong_count": session.get("wrong", 0) + 1
        })

# ─── ФРАЗЫ ───

@app.route("/phrases")
def phrases_page():
    return render_template("phrases.html", phrases=phrases)

@app.route("/phrases/add", methods=["POST"])
def phrases_add():
    data = request.json
    phrases[data["eng"]] = data["rus"]
    save_phrases()
    return jsonify({"status": "ok"})

@app.route("/phrases/delete", methods=["POST"])
def phrases_delete():
    data = request.json
    eng = data["eng"]
    if eng in phrases:
        del phrases[eng]
        save_phrases()
    return jsonify({"status": "ok"})

@app.route("/phrases/edit", methods=["POST"])
def phrases_edit():
    data = request.json
    old_eng = data["old_eng"]
    new_eng = data["new_eng"]
    new_rus = data["new_rus"]
    if old_eng in phrases:
        del phrases[old_eng]
        phrases[new_eng] = new_rus
        save_phrases()
    return jsonify({"status": "ok"})

@app.route("/phrases/train")
def phrases_train():
    if not phrases:
        return render_template("train_phrases.html", phrase=None, empty=True)
    eng = random.choice(list(phrases.keys()))
    session["current_phrase"] = eng
    return render_template("train_phrases.html", phrase=eng, empty=False)

@app.route("/phrases/check", methods=["POST"])
def phrases_check():
    data = request.json
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_phrase")
    if not eng or eng not in phrases:
        return jsonify({"status": "error"})
    correct_answer = phrases[eng].strip().lower()
    if user_answer == correct_answer:
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": phrases[eng],
            "correct_count": session.get("phrases_correct", 0) + 1,
            "wrong_count": session.get("phrases_wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": phrases[eng],
            "correct_count": session.get("phrases_correct", 0),
            "wrong_count": session.get("phrases_wrong", 0) + 1
        })

# ─── ПРОГРЕСС ───

@app.route("/progress")
def progress_page():
    total_words = len(words)
    total_phrases = len(phrases)
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
            "wrong": day_data["wrong"] if day_data else 0
        })

    max_day = max((d["correct"] + d["wrong"] for d in last_7), default=1)
    if max_day == 0:
        max_day = 1

    return render_template(
        "progress.html",
        total_words=total_words,
        total_phrases=total_phrases,
        total_correct=total_correct,
        total_wrong=total_wrong,
        accuracy=accuracy,
        streak=progress["streak"],
        last_7=last_7,
        max_day=max_day
    )

# ─── РЕЖИМ «НАОБОРОТ» ───

@app.route("/train_reverse")
def train_reverse():
    if not words:
        return render_template("train_reverse.html", word=None, empty=True)
    eng = random.choice(list(words.keys()))
    rus = words[eng]["rus"]
    session["current_reverse_eng"] = eng
    session["current_reverse_rus"] = rus
    return render_template("train_reverse.html", word=rus, empty=False)

@app.route("/check_reverse", methods=["POST"])
def check_reverse():
    data = request.json
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_reverse_eng")
    if not eng or eng not in words:
        return jsonify({"status": "error"})
    if user_answer == eng.lower():
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": eng,
            "correct_count": session.get("correct", 0) + 1,
            "wrong_count": session.get("wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng,
            "correct_count": session.get("correct", 0),
            "wrong_count": session.get("wrong", 0) + 1
        })

# ─── ТОПИКИ ───

FIXED_TOPICS = [
    {"id": "my_day", "title": "My Day", "emoji": "☀️", "helper": ["wake up", "breakfast", "work", "evening", "sleep", "morning", "lunch", "dinner"]},
    {"id": "my_family", "title": "My Family", "emoji": "👨‍👩‍👧", "helper": ["mother", "father", "brother", "sister", "love", "home", "parents", "children"]},
    {"id": "my_hobbies", "title": "My Hobbies", "emoji": "🎮", "helper": ["play", "read", "music", "sport", "game", "draw", "sing", "dance"]},
    {"id": "my_city", "title": "My City", "emoji": "🏙️", "helper": ["street", "park", "shop", "museum", "beautiful", "big", "small", "center"]},
    {"id": "my_dreams", "title": "My Dreams", "emoji": "💭", "helper": ["want", "future", "travel", "family", "success", "dream", "hope", "believe"]},
]

@app.route("/topics")
def topics_page():
    all_topics = []
    for t in FIXED_TOPICS:
        data = topics.get(t["id"], {})
        all_topics.append({
            "id": t["id"],
            "title": t["title"],
            "emoji": t["emoji"],
            "text": data.get("text", ""),
            "done": data.get("done", False),
            "word_count": len(data.get("text", "").split()) if data.get("text") else 0
        })
    for tid, data in topics.items():
        if tid.startswith("custom_"):
            all_topics.append({
                "id": tid,
                "title": data.get("title", "Своя тема"),
                "emoji": "📝",
                "text": data.get("text", ""),
                "done": data.get("done", False),
                "word_count": len(data.get("text", "").split()) if data.get("text") else 0
            })
    return render_template("topics.html", topics=all_topics)

@app.route("/topics/<tid>")
def topic_page(tid):
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    if not topic_info:
        if tid in topics:
            topic_info = {
                "id": tid,
                "title": topics[tid].get("title", "Своя тема"),
                "emoji": "📝",
                "helper": []
            }
        else:
            return "Тема не найдена", 404
    data = topics.get(tid, {"text": "", "done": False})
    return render_template(
        "topic.html",
        topic=topic_info,
        text=data.get("text", ""),
        done=data.get("done", False)
    )

@app.route("/topics/<tid>/save", methods=["POST"])
def topic_save(tid):
    data = request.json
    text = data["text"].strip()
    word_count = len(text.split())
    if word_count < 50:
        return jsonify({"status": "error", "message": "Минимум 50 слов"})
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    title = topic_info["title"] if topic_info else topics.get(tid, {}).get("title", "Своя тема")
    topics[tid] = {"title": title, "text": text, "done": True}
    save_topics()
    return jsonify({"status": "ok"})

@app.route("/topics/new", methods=["GET", "POST"])
def topic_new():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            return redirect("/topics/new")
        import time
        tid = "custom_" + str(int(time.time()))
        topics[tid] = {"title": title, "text": "", "done": False}
        save_topics()
        return redirect(f"/topics/{tid}")
    return render_template("topic_new.html")

@app.route("/topics/<tid>/delete", methods=["POST"])
def topic_delete(tid):
    if tid in topics and tid.startswith("custom_"):
        del topics[tid]
        save_topics()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
