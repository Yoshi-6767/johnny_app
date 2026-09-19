from flask import Flask, render_template, request, jsonify, session
import json
import random
import os
from datetime import date, timedelta

app = Flask(__name__)
app.secret_key = "johnny_english_secret_key_change_me"

WORDS_FILE = "words.json"
PHRASES_FILE = "phrases.json"
PROGRESS_FILE = "progress.json"

try:
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        words = json.load(f)
except:
    words = {"hello": "привет", "go": "идти", "cat": "кот"}

try:
    with open(PHRASES_FILE, "r", encoding="utf-8") as f:
        phrases = json.load(f)
except:
    phrases = {"How are you?": "Как дела?", "Thank you": "Спасибо"}

try:
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        progress = json.load(f)
except:
    progress = {"history": [], "streak": 0, "last_day": ""}

def save_words():
    with open(WORDS_FILE, "w", encoding="utf-8") as f:
        json.dump(words, f, ensure_ascii=False, indent=2)

def save_phrases():
    with open(PHRASES_FILE, "w", encoding="utf-8") as f:
        json.dump(phrases, f, ensure_ascii=False, indent=2)

def save_progress():
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)

def record_training(correct: bool):
    """Записывает тренировку в историю и обновляет стрик."""
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
    return render_template("index.html", words=words)

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    words[data["eng"]] = data["rus"]
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
    new_eng = data["new_eng"]
    new_rus = data["new_rus"]
    if old_eng in words:
        del words[old_eng]
        words[new_eng] = new_rus
        save_words()
    return jsonify({"status": "ok"})

@app.route("/train")
def train():
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
    correct_answer = words[eng].strip().lower()
    if user_answer == correct_answer:
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": words[eng],
            "correct_count": session.get("correct", 0) + 1,
            "wrong_count": session.get("wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": words[eng],
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

    # последние 7 дней
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
    # Берём русское слово (значение), показываем его, а ответ — английский (ключ)
    eng = random.choice(list(words.keys()))
    rus = words[eng]
    session["current_reverse_eng"] = eng
    session["current_reverse_rus"] = rus
    return render_template("train_reverse.html", word=rus, empty=False)

@app.route("/check_reverse", methods=["POST"])
def check_reverse():
    data = request.json
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_reverse_eng")
    rus = session.get("current_reverse_rus")
    if not eng or eng not in words:
        return jsonify({"status": "error"})
    # Правильный ответ — английское слово (ключ)
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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
