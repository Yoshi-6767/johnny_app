from flask import Flask, render_template, request, jsonify, session, redirect
import json
from deep_translator import MyMemoryTranslator
import random
import os
from datetime import date, timedelta

app = Flask(__name__)
app.secret_key = "flow_and_word_secret_key"

WORDS_FILE = "/data/words.json"
PHRASES_FILE = "/data/phrases.json"
PROGRESS_FILE = "/data/progress.json"
TOPICS_FILE = "/data/topics.json"
EXAM_FILE = "/data/exams.json"

# ─── КАТЕГОРИИ ───

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

# Слова — миграция из репозитория
DATA_EMPTY = False
try:
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        raw_words = json.load(f)
    if not raw_words:
        DATA_EMPTY = True
except:
    DATA_EMPTY = True

if DATA_EMPTY:
    try:
        with open("words.json", "r", encoding="utf-8") as f:
            raw_words = json.load(f)
        with open(WORDS_FILE, "w", encoding="utf-8") as f:
            json.dump(raw_words, f, ensure_ascii=False, indent=2)
    except:
        raw_words = {}

words = {}
for k, v in raw_words.items():
    if isinstance(v, dict):
        section = v.get("section", "general")
        if section not in [s["id"] for s in SECTIONS]:
            section = "general"
        words[k] = {"rus": v.get("rus", ""), "section": section}
    else:
        words[k] = {"rus": v, "section": "general"}

def save_words():
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

# Миграция фраз из репозитория
PHRASES_EMPTY = False
try:
    with open(PHRASES_FILE, "r", encoding="utf-8") as f:
        phrases = json.load(f)
    if not phrases:
        PHRASES_EMPTY = True
except:
    PHRASES_EMPTY = True

if PHRASES_EMPTY:
    try:
        with open("phrases.json", "r", encoding="utf-8") as f:
            phrases = json.load(f)
        with open(PHRASES_FILE, "w", encoding="utf-8") as f:
            json.dump(phrases, f, ensure_ascii=False, indent=2)
    except:
        phrases = {}

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

try:
    with open(EXAM_FILE, "r", encoding="utf-8") as f:
        exams = json.load(f)
except:
    exams = {}

def save_exams():
    with open(EXAM_FILE, "w", encoding="utf-8") as f:
        json.dump(exams, f, ensure_ascii=False, indent=2)

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

# ─── ГЛАВНАЯ ───

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

# ─── СЛОВА ───

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
        count = sum(1 for v in words.values() if v["section"] == s["id"])
        sections_data.append({
            "id": s["id"],
            "title": s["title"],
            "emoji": s["emoji"],
            "count": count
        })
    return render_template("sections.html", sections=sections_data, total_words=len(words))

@app.route("/sections/<sid>")
def section_page(sid):
    section = get_section(sid)
    section_words = {k: v for k, v in words.items() if v["section"] == sid}
    return render_template("section.html", section=section, words=section_words)

# ─── ТРЕНИРОВКА СЛОВ ───

@app.route("/train")
def train():
    section_id = request.args.get("section", "")
    reverse = request.args.get("reverse", "0") == "1"
    if section_id:
        filtered = {k: v for k, v in words.items() if v["section"] == section_id}
    else:
        filtered = words
    if not filtered:
        return render_template("train.html", word=None, empty=True, reverse=reverse, section=section_id)
    eng = random.choice(list(filtered.keys()))
    session["current_word"] = eng
    session["train_reverse"] = reverse
    session["train_section"] = section_id
    if reverse:
        display = filtered[eng]["rus"]
    else:
        display = eng
    return render_template("train.html", word=display, empty=False, reverse=reverse, section=section_id)

@app.route("/check", methods=["POST"])
def check():
    data = request.json
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_word")
    reverse = session.get("train_reverse", False)
    if not eng or eng not in words:
        return jsonify({"status": "error"})
    if reverse:
        correct_answer = eng.lower()
    else:
        correct_answer = words[eng]["rus"].strip().lower()
    if user_answer == correct_answer:
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": eng if reverse else words[eng]["rus"],
            "correct_count": session.get("correct", 0) + 1,
            "wrong_count": session.get("wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng if reverse else words[eng]["rus"],
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
    reverse = request.args.get("reverse", "0") == "1"
    if not phrases:
        return render_template("train_phrases.html", phrase=None, empty=True, reverse=reverse)
    eng = random.choice(list(phrases.keys()))
    session["current_phrase"] = eng
    session["phrase_reverse"] = reverse
    display = phrases[eng] if reverse else eng
    return render_template("train_phrases.html", phrase=display, empty=False, reverse=reverse)

@app.route("/phrases/check", methods=["POST"])
def phrases_check():
    data = request.json
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_phrase")
    reverse = session.get("phrase_reverse", False)
    if not eng or eng not in phrases:
        return jsonify({"status": "error"})
    if reverse:
        correct_answer = eng.lower()
    else:
        correct_answer = phrases[eng].strip().lower()
    if user_answer == correct_answer:
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": eng if reverse else phrases[eng],
            "correct_count": session.get("phrases_correct", 0) + 1,
            "wrong_count": session.get("phrases_wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng if reverse else phrases[eng],
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

# ─── ЭКЗАМЕН ───

@app.route("/exam")
def exam_page():
    all_topics = list(FIXED_TOPICS)
    for tid, data in topics.items():
        if tid.startswith("custom_"):
            all_topics.append({"id": tid, "title": data.get("title", "Своя тема"), "emoji": "📝", "helper": []})
    if not all_topics:
        return render_template("exam.html", topic=None, empty=True)
    topic = random.choice(all_topics)
    session["exam_topic"] = topic["id"]
    session["exam_start"] = str(date.today())
    return render_template("exam.html", topic=topic, empty=False)

@app.route("/exam/save", methods=["POST"])
def exam_save():
    data = request.json
    text = data["text"].strip()
    tid = session.get("exam_topic")
    if not tid:
        return jsonify({"status": "error"})
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    title = topic_info["title"] if topic_info else topics.get(tid, {}).get("title", "Своя тема")
    import time
    exam_id = str(int(time.time()))
    exams[exam_id] = {
        "topic_id": tid,
        "title": title,
        "text": text,
        "date": str(date.today()),
        "word_count": len(text.split())
    }
    save_exams()
    return jsonify({"status": "ok", "exam_id": exam_id})

@app.route("/exam/history")
def exam_history():
    exams_list = []
    for eid, data in sorted(exams.items(), key=lambda x: x[0], reverse=True):
        exams_list.append({
            "id": eid,
            "title": data["title"],
            "date": data["date"],
            "word_count": data["word_count"]
        })
    return render_template("exam_history.html", exams=exams_list)

# ─── ПЕРЕВОДЧИК ───

@app.route("/translator")
def translator_page():
    return render_template("translator.html")

@app.route("/translate", methods=["POST"])
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

# ─── FAQ ───

@app.route("/faq")
def faq_page():
    return render_template("faq.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
