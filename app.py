from flask import Flask, render_template, request, jsonify, session, redirect
import json
from deep_translator import MyMemoryTranslator
import random
import os
import time
from datetime import date, timedelta
from datetime import date as date_module

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

# ─── ЦИТАТЫ ДНЯ ───

QUOTES = [
    {"text": "The limits of my language mean the limits of my world.", "author": "Ludwig Wittgenstein"},
    {"text": "Learning is a treasure that will follow its owner everywhere.", "author": "Chinese Proverb"},
    {"text": "The more that you read, the more things you will know.", "author": "Dr. Seuss"},
    {"text": "To have another language is to possess a second soul.", "author": "Charlemagne"},
    {"text": "Language is the road map of a culture.", "author": "Rita Mae Brown"},
    {"text": "A different language is a different vision of life.", "author": "Federico Fellini"},
    {"text": "The best way to predict the future is to invent it.", "author": "Alan Kay"},
    {"text": "Success is the sum of small efforts repeated day in and day out.", "author": "Robert Collier"},
    {"text": "You are never too old to set another goal or to dream a new dream.", "author": "C.S. Lewis"},
    {"text": "The secret of getting ahead is getting started.", "author": "Mark Twain"},
    {"text": "Education is the most powerful weapon which you can use to change the world.", "author": "Nelson Mandela"},
    {"text": "The journey of a thousand miles begins with a single step.", "author": "Lao Tzu"},
    {"text": "Knowledge is power.", "author": "Francis Bacon"},
    {"text": "Practice makes perfect.", "author": "English Proverb"},
    {"text": "Where there is a will, there is a way.", "author": "English Proverb"},
    {"text": "Every day is a chance to get better.", "author": "Unknown"},
    {"text": "Don't watch the clock; do what it does. Keep going.", "author": "Sam Levenson"},
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "A word a day keeps the ignorance away.", "author": "Unknown"},
]

def get_daily_quote():
    today = date_module.today()
    day_of_year = today.timetuple().tm_yday
    return QUOTES[day_of_year % len(QUOTES)]

# ─── НЕПРАВИЛЬНЫЕ ГЛАГОЛЫ ───

IRREGULAR_VERBS = [
    {"base": "be", "past": "was/were", "pp": "been", "rus": "быть"},
    {"base": "become", "past": "became", "pp": "become", "rus": "становиться"},
    {"base": "begin", "past": "began", "pp": "begun", "rus": "начинать"},
    {"base": "break", "past": "broke", "pp": "broken", "rus": "ломать"},
    {"base": "bring", "past": "brought", "pp": "brought", "rus": "приносить"},
    {"base": "build", "past": "built", "pp": "built", "rus": "строить"},
    {"base": "buy", "past": "bought", "pp": "bought", "rus": "покупать"},
    {"base": "catch", "past": "caught", "pp": "caught", "rus": "ловить"},
    {"base": "choose", "past": "chose", "pp": "chosen", "rus": "выбирать"},
    {"base": "come", "past": "came", "pp": "come", "rus": "приходить"},
    {"base": "cost", "past": "cost", "pp": "cost", "rus": "стоить"},
    {"base": "cut", "past": "cut", "pp": "cut", "rus": "резать"},
    {"base": "do", "past": "did", "pp": "done", "rus": "делать"},
    {"base": "draw", "past": "drew", "pp": "drawn", "rus": "рисовать"},
    {"base": "drink", "past": "drank", "pp": "drunk", "rus": "пить"},
    {"base": "drive", "past": "drove", "pp": "driven", "rus": "водить"},
    {"base": "eat", "past": "ate", "pp": "eaten", "rus": "есть"},
    {"base": "fall", "past": "fell", "pp": "fallen", "rus": "падать"},
    {"base": "feel", "past": "felt", "pp": "felt", "rus": "чувствовать"},
    {"base": "fight", "past": "fought", "pp": "fought", "rus": "бороться"},
    {"base": "find", "past": "found", "pp": "found", "rus": "находить"},
    {"base": "fly", "past": "flew", "pp": "flown", "rus": "летать"},
    {"base": "forget", "past": "forgot", "pp": "forgotten", "rus": "забывать"},
    {"base": "get", "past": "got", "pp": "got/gotten", "rus": "получать"},
    {"base": "give", "past": "gave", "pp": "given", "rus": "давать"},
    {"base": "go", "past": "went", "pp": "gone", "rus": "идти"},
    {"base": "grow", "past": "grew", "pp": "grown", "rus": "расти"},
    {"base": "have", "past": "had", "pp": "had", "rus": "иметь"},
    {"base": "hear", "past": "heard", "pp": "heard", "rus": "слышать"},
    {"base": "hold", "past": "held", "pp": "held", "rus": "держать"},
    {"base": "keep", "past": "kept", "pp": "kept", "rus": "хранить"},
    {"base": "know", "past": "knew", "pp": "known", "rus": "знать"},
    {"base": "leave", "past": "left", "pp": "left", "rus": "уходить"},
    {"base": "lose", "past": "lost", "pp": "lost", "rus": "терять"},
    {"base": "make", "past": "made", "pp": "made", "rus": "делать"},
    {"base": "meet", "past": "met", "pp": "met", "rus": "встречать"},
    {"base": "pay", "past": "paid", "pp": "paid", "rus": "платить"},
    {"base": "put", "past": "put", "pp": "put", "rus": "класть"},
    {"base": "read", "past": "read", "pp": "read", "rus": "читать"},
    {"base": "ride", "past": "rode", "pp": "ridden", "rus": "ехать"},
    {"base": "run", "past": "ran", "pp": "run", "rus": "бегать"},
    {"base": "say", "past": "said", "pp": "said", "rus": "говорить"},
    {"base": "see", "past": "saw", "pp": "seen", "rus": "видеть"},
    {"base": "sell", "past": "sold", "pp": "sold", "rus": "продавать"},
    {"base": "send", "past": "sent", "pp": "sent", "rus": "отправлять"},
    {"base": "sing", "past": "sang", "pp": "sung", "rus": "петь"},
    {"base": "sit", "past": "sat", "pp": "sat", "rus": "сидеть"},
    {"base": "sleep", "past": "slept", "pp": "slept", "rus": "спать"},
    {"base": "speak", "past": "spoke", "pp": "spoken", "rus": "говорить"},
    {"base": "spend", "past": "spent", "pp": "spent", "rus": "тратить"},
    {"base": "stand", "past": "stood", "pp": "stood", "rus": "стоять"},
    {"base": "swim", "past": "swam", "pp": "swum", "rus": "плавать"},
    {"base": "take", "past": "took", "pp": "taken", "rus": "брать"},
    {"base": "teach", "past": "taught", "pp": "taught", "rus": "учить"},
    {"base": "tell", "past": "told", "pp": "told", "rus": "рассказывать"},
    {"base": "think", "past": "thought", "pp": "thought", "rus": "думать"},
    {"base": "understand", "past": "understood", "pp": "understood", "rus": "понимать"},
    {"base": "wake", "past": "woke", "pp": "woken", "rus": "просыпаться"},
    {"base": "wear", "past": "wore", "pp": "worn", "rus": "носить"},
    {"base": "win", "past": "won", "pp": "won", "rus": "побеждать"},
    {"base": "write", "past": "wrote", "pp": "written", "rus": "писать"},
]

# ─── ЗАГРУЗКА ДАННЫХ ───

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
        streak=streak,
        quote=get_daily_quote()
    )

# ─── СЛОВА ───

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

# ─── КАТЕГОРИИ ───

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

# ─── УЧЁБА ───

@app.route("/study")
def study_page():
    return render_template("study.html")

@app.route("/study/irregular")
def irregular_page():
    return render_template("irregular.html", verbs=IRREGULAR_VERBS)

@app.route("/study/irregular/train")
def irregular_train():
    mode = request.args.get("mode", "past")
    if not IRREGULAR_VERBS:
        return render_template("irregular_train.html", empty=True)
    session["irr_mode"] = mode
    session["irr_correct"] = 0
    session["irr_wrong"] = 0
    session["irr_used"] = []
    return render_template("irregular_train.html", empty=False, mode=mode)

@app.route("/study/irregular/next")
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
        return jsonify({
            "status": "ok",
            "question": verb["base"],
            "question_label": "Base → Past",
            "hint": "Какая форма Past?"
        })
    elif mode == "pp":
        return jsonify({
            "status": "ok",
            "question": verb["base"],
            "question_label": "Base → Past Participle",
            "hint": "Какая форма Past Participle?"
        })
    else:
        form = random.choice(["past", "pp"])
        session["irr_mixed_form"] = form
        if form == "past":
            return jsonify({
                "status": "ok",
                "question": verb["base"],
                "question_label": "Base → Past",
                "hint": "Какая форма Past?"
            })
        else:
            return jsonify({
                "status": "ok",
                "question": verb["pp"],
                "question_label": "Past Participle → Base",
                "hint": "Какой это глагол?"
            })

@app.route("/study/irregular/check", methods=["POST"])
def irregular_check():
    data = request.json
    answer = data.get("answer", "").strip().lower()
    base = session.get("irr_current", "")
    mode = session.get("irr_mode", "past")
    verb = next((v for v in IRREGULAR_VERBS if v["base"] == base), None)
    if not verb:
        return jsonify({"status": "error"})

    if mode == "past":
        correct = verb["past"].lower()
        correct_display = verb["past"]
    elif mode == "pp":
        correct = verb["pp"].lower()
        correct_display = verb["pp"]
    else:
        form = session.get("irr_mixed_form", "past")
        if form == "past":
            correct = verb["past"].lower()
            correct_display = verb["past"]
        else:
            correct = verb["base"].lower()
            correct_display = verb["base"]

    is_correct = answer == correct
    if is_correct:
        session["irr_correct"] = session.get("irr_correct", 0) + 1
    else:
        session["irr_wrong"] = session.get("irr_wrong", 0) + 1

    return jsonify({
        "status": "ok",
        "correct": is_correct,
        "correct_answer": correct_display,
        "score": session.get("irr_correct", 0),
        "wrong": session.get("irr_wrong", 0)
    })

# ─── ИГРОВЫЕ РЕЖИМЫ ───

HANGMAN_STATE = {}

@app.route("/games")
def games_page():
    return render_template("games.html")

@app.route("/games/hangman")
def hangman_page():
    available = [w for w in words.keys() if 4 <= len(w) <= 12 and " " not in w]
    if not available:
        return render_template("hangman.html", empty=True)
    word = random.choice(available).lower()
    section_id = words[word]["section"]
    section = next((s for s in SECTIONS if s["id"] == section_id), SECTIONS[-1])
    session["hangman_word"] = word
    session["hangman_guessed"] = []
    session["hangman_errors"] = 0
    display = " ".join(["_" for _ in word])
    return render_template(
        "hangman.html",
        empty=False,
        display=display,
        errors=0,
        max_errors=6,
        guessed=[],
        word_length=len(word),
        section=section
    )

@app.route("/games/hangman/guess", methods=["POST"])
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
            "errors": errors,
            "guessed": guessed,
            "message": "Эту букву уже называл"
        })

    guessed.append(letter)
    if letter not in word:
        errors += 1

    session["hangman_guessed"] = guessed
    session["hangman_errors"] = errors

    display = " ".join([c if c in guessed else "_" for c in word])

    if all(c in guessed for c in word):
        return jsonify({
            "status": "win",
            "display": display,
            "word": word,
            "errors": errors,
            "guessed": guessed,
            "message": "🎉 Ты угадал! Слово: " + word
        })

    if errors >= 6:
        return jsonify({
            "status": "lose",
            "display": display,
            "word": word,
            "errors": errors,
            "guessed": guessed,
            "message": "💀 Ты проиграл. Слово было: " + word
        })

    return jsonify({
        "status": "ok",
        "display": display,
        "errors": errors,
        "guessed": guessed
    })

# ─── КВИЗ ───

QUIZ_STATE = {}

@app.route("/games/quiz")
def quiz_page():
    available = [w for w in words.keys() if 4 <= len(w) <= 12 and " " not in w]
    if len(available) < 4:
        return render_template("quiz.html", empty=True)
    session["quiz_score"] = 0
    session["quiz_question"] = 0
    session["quiz_total"] = 10
    session["quiz_used"] = []
    session["quiz_errors"] = []
    return render_template("quiz.html", empty=False)

@app.route("/games/quiz/question")
def quiz_question():
    available = [w for w in words.keys() if 4 <= len(w) <= 12 and " " not in w and w not in session.get("quiz_used", [])]
    if not available:
        return jsonify({"status": "end"})

    word = random.choice(available)
    session["quiz_used"] = session.get("quiz_used", []) + [word]
    session["quiz_current"] = word

    correct = words[word]["rus"]

    others = [w for w in words.keys() if w != word and words[w]["rus"] != correct]
    wrong_options = random.sample(others, min(3, len(others)))
    wrong_answers = [words[w]["rus"] for w in wrong_options]

    options = [correct] + wrong_answers
    random.shuffle(options)

    question_num = session.get("quiz_question", 0) + 1
    session["quiz_question"] = question_num

    return jsonify({
        "status": "ok",
        "word": word,
        "options": options,
        "correct": correct,
        "question_num": question_num,
        "total": session.get("quiz_total", 10)
    })

@app.route("/games/quiz/answer", methods=["POST"])
def quiz_answer():
    data = request.json
    answer = data.get("answer", "").strip()
    word = session.get("quiz_current", "")
    if not word or word not in words:
        return jsonify({"status": "error"})

    correct = words[word]["rus"]
    is_correct = (answer == correct)

    if is_correct:
        session["quiz_score"] = session.get("quiz_score", 0) + 1
    else:
        errors = session.get("quiz_errors", [])
        errors.append({"word": word, "correct": correct, "chosen": answer})
        session["quiz_errors"] = errors

    return jsonify({
        "status": "ok",
        "correct": is_correct,
        "correct_answer": correct,
        "score": session.get("quiz_score", 0)
    })

@app.route("/games/quiz/result")
def quiz_result():
    score = session.get("quiz_score", 0)
    total = session.get("quiz_total", 10)
    errors = session.get("quiz_errors", [])
    return jsonify({
        "score": score,
        "total": total,
        "errors": errors
    })

# ─── СКОРОСТНОЙ РЕЖИМ ───

@app.route("/games/speed")
def speed_page():
    available = [w for w in words.keys() if 2 <= len(w) <= 15]
    if len(available) < 5:
        return render_template("speed.html", empty=True)
    return render_template("speed.html", empty=False)

@app.route("/games/speed/start")
def speed_start():
    available = [w for w in words.keys() if 2 <= len(w) <= 15]
    if len(available) < 5:
        return jsonify({"status": "error"})
    chosen = random.sample(available, min(10, len(available)))
    session["speed_words"] = chosen
    session["speed_index"] = 0
    session["speed_score"] = 0
    session["speed_start"] = time.time()
    return jsonify({"status": "ok", "total": len(chosen)})

@app.route("/games/speed/next")
def speed_next():
    speed_words = session.get("speed_words", [])
    index = session.get("speed_index", 0)
    if index >= len(speed_words):
        return jsonify({"status": "end"})
    word = speed_words[index]
    return jsonify({
        "status": "ok",
        "word": word,
        "index": index + 1,
        "total": len(speed_words)
    })

@app.route("/games/speed/check", methods=["POST"])
def speed_check():
    data = request.json
    answer = data.get("answer", "").strip().lower()
    speed_words = session.get("speed_words", [])
    index = session.get("speed_index", 0)
    if index >= len(speed_words):
        return jsonify({"status": "error"})
    word = speed_words[index]
    correct = words[word]["rus"].strip().lower()
    is_correct = (answer == correct)
    if is_correct:
        session["speed_score"] = session.get("speed_score", 0) + 1
    session["speed_index"] = index + 1
    return jsonify({
        "status": "ok",
        "correct": is_correct,
        "correct_answer": words[word]["rus"],
        "score": session.get("speed_score", 0),
        "index": index + 1,
        "total": len(speed_words)
    })

@app.route("/games/speed/result")
def speed_result():
    return jsonify({
        "score": session.get("speed_score", 0),
        "total": len(session.get("speed_words", []))
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
