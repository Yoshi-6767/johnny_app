from flask import Flask, render_template, request, jsonify, session, redirect, url_for, Response
import json
from deep_translator import MyMemoryTranslator
import random
import os
import time
from datetime import date, timedelta
from datetime import date as date_module
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = "flow_and_word_secret_key"

# ─── БАЗА ДАННЫХ ───
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ─── АВТОРИЗАЦИЯ ───
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)

class EmailCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=date_module.today)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

# ─── SMTP ЯНДЕКС ───
SMTP_SERVER = "smtp.yandex.ru"
SMTP_PORT = 587
SMTP_USER = "DiKeyTokyo@yandex.ru"
SMTP_PASSWORD = "lljmhqxxvbhahwtp"

def send_verification_code(to_email, code):
    msg = MIMEText(f"Твой код подтверждения: {code}\n\nКод действует 15 минут.")
    msg['Subject'] = 'Подтверждение регистрации — Flow & Word'
    msg['From'] = SMTP_USER
    msg['To'] = to_email
    
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(SMTP_USER, SMTP_PASSWORD)
    server.send_message(msg)
    server.quit()

# ─── КАТЕГОРИИ ───

SECTIONS = [
    {"id": "family", "title": "Family", "emoji": "👨‍👩‍👧", "level": "A1-A2"},
    {"id": "home", "title": "Home", "emoji": "🏠", "level": "A1-A2"},
    {"id": "routine", "title": "Daily Routine", "emoji": "⏰", "level": "A1-A2"},
    {"id": "food", "title": "Food", "emoji": "🍔", "level": "A1-A2"},
    {"id": "clothes", "title": "Clothes", "emoji": "👕", "level": "A1-A2"},
    {"id": "appearance", "title": "Appearance", "emoji": "👤", "level": "A1-A2"},
    {"id": "weather", "title": "Weather", "emoji": "☀️", "level": "A1-A2"},
    {"id": "transport", "title": "Transport", "emoji": "🚗", "level": "A1-A2"},
    {"id": "work", "title": "Work", "emoji": "💼", "level": "A1-A2"},
    {"id": "health", "title": "Health", "emoji": "💊", "level": "A1-A2"},
    {"id": "shopping", "title": "Shopping", "emoji": "🛒", "level": "A1-A2"},
    {"id": "holidays", "title": "Holidays", "emoji": "🏖️", "level": "A1-A2"},
    {"id": "feelings", "title": "Feelings", "emoji": "😊", "level": "B1"},
    {"id": "character", "title": "Character", "emoji": "🎭", "level": "B1"},
    {"id": "relationships", "title": "Relationships", "emoji": "💕", "level": "B1"},
    {"id": "communication", "title": "Communication", "emoji": "💬", "level": "B1"},
    {"id": "money", "title": "Money & Business", "emoji": "💰", "level": "B1"},
    {"id": "technology", "title": "Technology", "emoji": "💻", "level": "B1"},
    {"id": "education", "title": "Education", "emoji": "🎓", "level": "B1"},
    {"id": "media", "title": "Media", "emoji": "📰", "level": "B1"},
    {"id": "city", "title": "City & Town", "emoji": "🏙️", "level": "B1"},
    {"id": "nature", "title": "Nature", "emoji": "🌳", "level": "B1"},
    {"id": "time", "title": "Time", "emoji": "🕐", "level": "B1"},
    {"id": "housework", "title": "Housework", "emoji": "🧹", "level": "B1"},
    {"id": "business", "title": "Business & Negotiations", "emoji": "🤝", "level": "B2+"},
    {"id": "politics", "title": "Politics & Law", "emoji": "⚖️", "level": "B2+"},
    {"id": "environment", "title": "Environment", "emoji": "🌍", "level": "B2+"},
    {"id": "art", "title": "Art & Culture", "emoji": "🎨", "level": "B2+"},
    {"id": "science", "title": "Science", "emoji": "🔬", "level": "B2+"},
    {"id": "general", "title": "Общее", "emoji": "📦", "level": "general"},
]

def get_section(sid):
    return next((s for s in SECTIONS if s["id"] == sid), SECTIONS[-1])

# ─── ЗАГРУЗКА ОБЩИХ СЛОВ ───

WORDS_FILE = "words.json"
try:
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        common_words = json.load(f)
except:
    common_words = {}

# ─── ХРАНИЛИЩЕ ПОЛЬЗОВАТЕЛЕЙ ───

users_data = {}

def get_user_data(user_id):
    if user_id not in users_data:
        users_data[user_id] = {
            "general_words": {},
            "phrases": {},
            "progress": {"history": [], "streak": 0, "last_day": "", "weak_words": {}},
            "topics": {},
            "exams": {}
        }
    return users_data[user_id]

def get_all_words(user_id):
    """Общие слова + личные (general)"""
    user_data = get_user_data(user_id)
    all_w = {}
    for k, v in common_words.items():
        all_w[k] = v
    for k, v in user_data["general_words"].items():
        all_w[k] = v
    return all_w

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

# ─── ФРАЗОВЫЕ ГЛАГОЛЫ ───

PHRASAL_VERBS = [
    {"phrase": "give up", "rus": "бросить", "example": "I gave up smoking."},
    {"phrase": "look after", "rus": "заботиться", "example": "She looks after her sister."},
    {"phrase": "run out of", "rus": "закончиться", "example": "We ran out of milk."},
    {"phrase": "find out", "rus": "выяснить", "example": "I found out the truth."},
    {"phrase": "come back", "rus": "вернуться", "example": "He came back home."},
    {"phrase": "go on", "rus": "продолжать", "example": "Go on, tell me!"},
    {"phrase": "turn off", "rus": "выключить", "example": "Turn off the light."},
    {"phrase": "turn on", "rus": "включить", "example": "Turn on the TV."},
    {"phrase": "put on", "rus": "надеть", "example": "Put on your coat."},
    {"phrase": "take off", "rus": "снять", "example": "Take off your shoes."},
    {"phrase": "wake up", "rus": "проснуться", "example": "I wake up at 7."},
    {"phrase": "get up", "rus": "встать", "example": "Get up, sleepyhead!"},
    {"phrase": "sit down", "rus": "сесть", "example": "Sit down, please."},
    {"phrase": "stand up", "rus": "встать", "example": "Stand up straight."},
    {"phrase": "come in", "rus": "войти", "example": "Come in!"},
    {"phrase": "go out", "rus": "выйти", "example": "We go out on Fridays."},
    {"phrase": "look for", "rus": "искать", "example": "I'm looking for my keys."},
    {"phrase": "look forward to", "rus": "ждать с нетерпением", "example": "I look forward to seeing you."},
    {"phrase": "give back", "rus": "вернуть", "example": "Give back my book."},
    {"phrase": "take care of", "rus": "заботиться", "example": "Take care of yourself."},
    {"phrase": "get along with", "rus": "ладить", "example": "I get along with my brother."},
    {"phrase": "break down", "rus": "сломаться", "example": "My car broke down."},
    {"phrase": "carry on", "rus": "продолжать", "example": "Carry on with your work."},
    {"phrase": "check out", "rus": "проверить", "example": "Check out this song."},
    {"phrase": "figure out", "rus": "разобраться", "example": "I figured out the puzzle."},
    {"phrase": "grow up", "rus": "вырасти", "example": "I grew up in Moscow."},
    {"phrase": "hang out", "rus": "тусоваться", "example": "Let's hang out tomorrow."},
    {"phrase": "hold on", "rus": "подождать", "example": "Hold on a second."},
    {"phrase": "keep on", "rus": "продолжать", "example": "Keep on trying."},
    {"phrase": "move on", "rus": "двигаться дальше", "example": "Let's move on."},
    {"phrase": "pick up", "rus": "подобрать", "example": "Pick up the phone."},
    {"phrase": "point out", "rus": "указать", "example": "He pointed out my mistake."},
    {"phrase": "put off", "rus": "отложить", "example": "Put off the meeting."},
    {"phrase": "set up", "rus": "установить", "example": "Set up the tent."},
    {"phrase": "show up", "rus": "появиться", "example": "He showed up late."},
    {"phrase": "take over", "rus": "взять контроль", "example": "She took over the project."},
    {"phrase": "throw away", "rus": "выбросить", "example": "Throw away the trash."},
    {"phrase": "try on", "rus": "примерить", "example": "Try on this dress."},
    {"phrase": "work out", "rus": "тренироваться", "example": "I work out every day."},
    {"phrase": "write down", "rus": "записать", "example": "Write down the address."},
]

# ─── ИДИОМЫ ───

IDIOMS = [
    {"idiom": "break a leg", "rus": "ни пуха, ни пера", "literal": "сломай ногу"},
    {"idiom": "piece of cake", "rus": "проще простого", "literal": "кусок торта"},
    {"idiom": "hit the books", "rus": "засесть за учёбу", "literal": "ударить книги"},
    {"idiom": "under the weather", "rus": "неважно себя чувствовать", "literal": "под погодой"},
    {"idiom": "once in a blue moon", "rus": "очень редко", "literal": "раз в голубую луну"},
    {"idiom": "spill the beans", "rus": "проболтаться", "literal": "пролить бобы"},
    {"idiom": "cost an arm and a leg", "rus": "стоить очень дорого", "literal": "стоить руку и ногу"},
    {"idiom": "let the cat out of the bag", "rus": "раскрыть секрет", "literal": "выпустить кота из мешка"},
    {"idiom": "kill two birds with one stone", "rus": "убить двух зайцев", "literal": "убить двух птиц одним камнем"},
    {"idiom": "the ball is in your court", "rus": "твой ход", "literal": "мяч на твоём корте"},
    {"idiom": "bite the bullet", "rus": "стиснуть зубы", "literal": "укусить пулю"},
    {"idiom": "break the ice", "rus": "растопить лёд", "literal": "сломать лёд"},
    {"idiom": "cut corners", "rus": "халтурить", "literal": "резать углы"},
    {"idiom": "hit the sack", "rus": "пойти спать", "literal": "ударить мешок"},
    {"idiom": "it's raining cats and dogs", "rus": "льёт как из ведра", "literal": "дождь из кошек и собак"},
    {"idiom": "let sleeping dogs lie", "rus": "не буди лихо", "literal": "дай спящим собакам лежать"},
    {"idiom": "miss the boat", "rus": "упустить шанс", "literal": "пропустить лодку"},
    {"idiom": "on cloud nine", "rus": "на седьмом небе", "literal": "на девятом облаке"},
    {"idiom": "pull yourself together", "rus": "возьми себя в руки", "literal": "собери себя вместе"},
    {"idiom": "see eye to eye", "rus": "сходиться во мнениях", "literal": "видеть глаз в глаз"},
    {"idiom": "sit on the fence", "rus": "занимать нейтралитет", "literal": "сидеть на заборе"},
    {"idiom": "take it easy", "rus": "не напрягайся", "literal": "принимай это легко"},
    {"idiom": "the last straw", "rus": "последняя капля", "literal": "последняя соломинка"},
    {"idiom": "time flies", "rus": "время летит", "literal": "время летает"},
    {"idiom": "under your nose", "rus": "прямо под носом", "literal": "под твоим носом"},
    {"idiom": "when pigs fly", "rus": "когда рак на горе свистнет", "literal": "когда свиньи полетят"},
    {"idiom": "you can't judge a book by its cover", "rus": "не суди по обложке", "literal": "нельзя судить книгу по обложке"},
    {"idiom": "actions speak louder than words", "rus": "дела говорят громче слов", "literal": "действия говорят громче слов"},
    {"idiom": "better late than never", "rus": "лучше поздно, чем никогда", "literal": "лучше поздно, чем никогда"},
    {"idiom": "easier said than done", "rus": "легко сказать, да трудно сделать", "literal": "легче сказать, чем сделать"},
]

# ─── ГЛАВНАЯ ───

@app.route("/")
def index():
    if current_user.is_authenticated:
        user_data = get_user_data(current_user.id)
        all_w = get_all_words(current_user.id)
        total_words = len(all_w)
        total_phrases = len(user_data["phrases"])
        total_topics_done = sum(1 for t in user_data["topics"].values() if t.get("done"))
        total_topics = len(FIXED_TOPICS) + sum(1 for t in user_data["topics"].keys() if t.startswith("custom_"))
        streak = user_data["progress"].get("streak", 0)
    else:
        total_words = len(common_words)
        total_phrases = 0
        total_topics_done = 0
        total_topics = len(FIXED_TOPICS)
        streak = 0
    
    return render_template(
        "index.html",
        total_words=total_words,
        total_phrases=total_phrases,
        total_topics_done=total_topics_done,
        total_topics=total_topics,
        streak=streak,
        quote=get_daily_quote()
    )

# ─── СЛОВА (только general) ───

@app.route("/add", methods=["POST"])
@login_required
def add():
    data = request.json
    user_data = get_user_data(current_user.id)
    eng = data["eng"].strip()
    rus = data["rus"].strip()
    section = data.get("section", "general")
    if section != "general":
        return jsonify({"status": "error", "message": "Можно добавлять только в «Общее»"})
    user_data["general_words"][eng] = {"rus": rus, "section": "general"}
    return jsonify({"status": "ok"})

@app.route("/delete", methods=["POST"])
@login_required
def delete():
    data = request.json
    user_data = get_user_data(current_user.id)
    eng = data["eng"]
    if eng in user_data["general_words"]:
        del user_data["general_words"][eng]
    return jsonify({"status": "ok"})

@app.route("/edit", methods=["POST"])
@login_required
def edit():
    data = request.json
    user_data = get_user_data(current_user.id)
    old_eng = data["old_eng"]
    new_eng = data["new_eng"].strip()
    new_rus = data["new_rus"].strip()
    if old_eng in user_data["general_words"]:
        del user_data["general_words"][old_eng]
        user_data["general_words"][new_eng] = {"rus": new_rus, "section": "general"}
    return jsonify({"status": "ok"})

# ─── КАТЕГОРИИ ───

@app.route("/sections")
@login_required
def sections_page():
    user_data = get_user_data(current_user.id)
    sections_data = []
    for s in SECTIONS:
        if s["id"] == "general":
            count = len(user_data["general_words"])
        else:
            count = sum(1 for v in common_words.values() if v.get("section") == s["id"])
        sections_data.append({
            "id": s["id"],
            "title": s["title"],
            "emoji": s["emoji"],
            "count": count,
            "level": s.get("level", "general")
        })
    all_w = get_all_words(current_user.id)
    return render_template("sections.html", sections=sections_data, total_words=len(all_w))

@app.route("/sections/<sid>")
@login_required
def section_page(sid):
    user_data = get_user_data(current_user.id)
    section = get_section(sid)
    if sid == "general":
        section_words = user_data["general_words"]
    else:
        section_words = {k: v for k, v in common_words.items() if v.get("section") == sid}
    return render_template("section.html", section=section, words=section_words)

# ─── ТРЕНИРОВКА ───

@app.route("/train")
@login_required
def train():
    user_data = get_user_data(current_user.id)
    section_id = request.args.get("section", "")
    reverse = request.args.get("reverse", "0") == "1"
    if section_id:
        if section_id == "general":
            filtered = user_data["general_words"]
        else:
            filtered = {k: v for k, v in common_words.items() if v.get("section") == section_id}
    else:
        filtered = get_all_words(current_user.id)
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
@login_required
def check():
    data = request.json
    all_w = get_all_words(current_user.id)
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_word")
    reverse = session.get("train_reverse", False)
    if not eng or eng not in all_w:
        return jsonify({"status": "error"})
    if reverse:
        correct_answer = eng.lower()
    else:
        correct_answer = all_w[eng]["rus"].strip().lower()
    if user_answer == correct_answer:
        record_training(True, eng)
        return jsonify({
            "status": "correct",
            "correct_answer": eng if reverse else all_w[eng]["rus"],
            "correct_count": session.get("correct", 0) + 1,
            "wrong_count": session.get("wrong", 0)
        })
    else:
        record_training(False, eng)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng if reverse else all_w[eng]["rus"],
            "correct_count": session.get("correct", 0),
            "wrong_count": session.get("wrong", 0) + 1
        })

# ─── ФРАЗЫ ───

@app.route("/phrases")
@login_required
def phrases_page():
    user_data = get_user_data(current_user.id)
    return render_template("phrases.html", phrases=user_data["phrases"])

@app.route("/phrases/add", methods=["POST"])
@login_required
def phrases_add():
    data = request.json
    user_data = get_user_data(current_user.id)
    user_data["phrases"][data["eng"]] = data["rus"]
    return jsonify({"status": "ok"})

@app.route("/phrases/delete", methods=["POST"])
@login_required
def phrases_delete():
    data = request.json
    user_data = get_user_data(current_user.id)
    eng = data["eng"]
    if eng in user_data["phrases"]:
        del user_data["phrases"][eng]
    return jsonify({"status": "ok"})

@app.route("/phrases/edit", methods=["POST"])
@login_required
def phrases_edit():
    data = request.json
    user_data = get_user_data(current_user.id)
    old_eng = data["old_eng"]
    new_eng = data["new_eng"]
    new_rus = data["new_rus"]
    if old_eng in user_data["phrases"]:
        del user_data["phrases"][old_eng]
        user_data["phrases"][new_eng] = new_rus
    return jsonify({"status": "ok"})

@app.route("/phrases/train")
@login_required
def phrases_train():
    user_data = get_user_data(current_user.id)
    reverse = request.args.get("reverse", "0") == "1"
    if not user_data["phrases"]:
        return render_template("train_phrases.html", phrase=None, empty=True, reverse=reverse)
    eng = random.choice(list(user_data["phrases"].keys()))
    session["current_phrase"] = eng
    session["phrase_reverse"] = reverse
    display = user_data["phrases"][eng] if reverse else eng
    return render_template("train_phrases.html", phrase=display, empty=False, reverse=reverse)

@app.route("/phrases/check", methods=["POST"])
@login_required
def phrases_check():
    data = request.json
    user_data = get_user_data(current_user.id)
    user_answer = data["answer"].strip().lower()
    eng = session.get("current_phrase")
    reverse = session.get("phrase_reverse", False)
    if not eng or eng not in user_data["phrases"]:
        return jsonify({"status": "error"})
    if reverse:
        correct_answer = eng.lower()
    else:
        correct_answer = user_data["phrases"][eng].strip().lower()
    if user_answer == correct_answer:
        record_training(True)
        return jsonify({
            "status": "correct",
            "correct_answer": eng if reverse else user_data["phrases"][eng],
            "correct_count": session.get("phrases_correct", 0) + 1,
            "wrong_count": session.get("phrases_wrong", 0)
        })
    else:
        record_training(False)
        return jsonify({
            "status": "wrong",
            "correct_answer": eng if reverse else user_data["phrases"][eng],
            "correct_count": session.get("phrases_correct", 0),
            "wrong_count": session.get("phrases_wrong", 0) + 1
        })

# ─── ПРОГРЕСС ───

@app.route("/progress")
@login_required
def progress_page():
    user_data = get_user_data(current_user.id)
    user_progress = user_data["progress"]
    all_w = get_all_words(current_user.id)
    total_words = len(all_w)
    total_phrases = len(user_data["phrases"])
    total_correct = sum(d["correct"] for d in user_progress["history"])
    total_wrong = sum(d["wrong"] for d in user_progress["history"])
    total_answers = total_correct + total_wrong
    accuracy = round(total_correct / total_answers * 100) if total_answers > 0 else 0

    last_7 = []
    for i in range(6, -1, -1):
        day = str(date.today() - timedelta(days=i))
        day_data = next((d for d in user_progress["history"] if d["date"] == day), None)
        last_7.append({
            "date": day,
            "label": day[8:10] + "." + day[5:7],
            "correct": day_data["correct"] if day_data else 0,
            "wrong": day_data["wrong"] if day_data else 0
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
    for i in range(first_weekday):
        calendar_days.append({"empty": True})
    for day_num in range(1, days_in_month + 1):
        day_str = str(today.replace(day=day_num))
        trained = any(d["date"] == day_str and (d["correct"] + d["wrong"]) > 0 for d in user_progress["history"])
        is_today = (day_num == today.day)
        calendar_days.append({
            "empty": False,
            "day": day_num,
            "trained": trained,
            "today": is_today
        })

    weak_words = user_progress.get("weak_words", {})
    weak_sorted = sorted(weak_words.items(), key=lambda x: x[1], reverse=True)[:10]
    weak_list = []
    for w, count in weak_sorted:
        if w in all_w:
            weak_list.append({"word": w, "rus": all_w[w]["rus"], "count": count})

    return render_template(
        "progress.html",
        total_words=total_words,
        total_phrases=total_phrases,
        total_correct=total_correct,
        total_wrong=total_wrong,
        accuracy=accuracy,
        streak=user_progress["streak"],
        last_7=last_7,
        max_day=max_day,
        calendar_days=calendar_days,
        weak_words=weak_list,
        month_name=today.strftime("%B %Y")
    )

# ─── ЗАПИСЬ ТРЕНИРОВКИ ───

def record_training(correct: bool, word=None):
    user_data = get_user_data(current_user.id)
    progress = user_data["progress"]
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

    if word and not correct:
        if "weak_words" not in progress:
            progress["weak_words"] = {}
        progress["weak_words"][word] = progress["weak_words"].get(word, 0) + 1

# ─── ТОПИКИ ───

FIXED_TOPICS = [
    {"id": "my_day", "title": "My Day", "emoji": "☀️", "helper": ["wake up", "breakfast", "work", "evening", "sleep", "morning", "lunch", "dinner"]},
    {"id": "my_family", "title": "My Family", "emoji": "👨‍👩‍👧", "helper": ["mother", "father", "brother", "sister", "love", "home", "parents", "children"]},
    {"id": "my_hobbies", "title": "My Hobbies", "emoji": "🎮", "helper": ["play", "read", "music", "sport", "game", "draw", "sing", "dance"]},
    {"id": "my_city", "title": "My City", "emoji": "🏙️", "helper": ["street", "park", "shop", "museum", "beautiful", "big", "small", "center"]},
    {"id": "my_dreams", "title": "My Dreams", "emoji": "💭", "helper": ["want", "future", "travel", "family", "success", "dream", "hope", "believe"]},
    {"id": "my_job", "title": "My Job", "emoji": "💼", "helper": ["office", "boss", "meeting", "colleague", "task", "project", "career", "salary"]},
    {"id": "my_travels", "title": "My Travels", "emoji": "✈️", "helper": ["airport", "ticket", "hotel", "luggage", "passport", "flight", "beach", "tourist"]},
    {"id": "my_food", "title": "My Food", "emoji": "🍕", "helper": ["breakfast", "lunch", "dinner", "tasty", "cook", "restaurant", "hungry", "delicious"]},
    {"id": "my_health", "title": "My Health", "emoji": "💪", "helper": ["sport", "gym", "doctor", "healthy", "sleep", "water", "vitamins", "energy"]},
    {"id": "my_future", "title": "My Future", "emoji": "🚀", "helper": ["career", "family", "travel", "success", "dream", "plan", "goal", "achieve"]},
]

@app.route("/topics")
@login_required
def topics_page():
    user_data = get_user_data(current_user.id)
    user_topics = user_data["topics"]
    all_topics = []
    for t in FIXED_TOPICS:
        data = user_topics.get(t["id"], {})
        all_topics.append({
            "id": t["id"],
            "title": t["title"],
            "emoji": t["emoji"],
            "text": data.get("text", ""),
            "done": data.get("done", False),
            "word_count": len(data.get("text", "").split()) if data.get("text") else 0
        })
    for tid, data in user_topics.items():
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
@login_required
def topic_page(tid):
    user_data = get_user_data(current_user.id)
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    if not topic_info:
        if tid in user_data["topics"]:
            topic_info = {
                "id": tid,
                "title": user_data["topics"][tid].get("title", "Своя тема"),
                "emoji": "📝",
                "helper": []
            }
        else:
            return "Тема не найдена", 404
    data = user_data["topics"].get(tid, {"text": "", "done": False})
    return render_template(
        "topic.html",
        topic=topic_info,
        text=data.get("text", ""),
        done=data.get("done", False)
    )

@app.route("/topics/<tid>/save", methods=["POST"])
@login_required
def topic_save(tid):
    user_data = get_user_data(current_user.id)
    data = request.json
    text = data["text"].strip()
    word_count = len(text.split())
    if word_count < 50:
        return jsonify({"status": "error", "message": "Минимум 50 слов"})
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    title = topic_info["title"] if topic_info else user_data["topics"].get(tid, {}).get("title", "Своя тема")
    user_data["topics"][tid] = {"title": title, "text": text, "done": True}
    return jsonify({"status": "ok"})

@app.route("/topics/new", methods=["GET", "POST"])
@login_required
def topic_new():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if not title:
            return redirect("/topics/new")
        tid = "custom_" + str(int(time.time()))
        user_data = get_user_data(current_user.id)
        user_data["topics"][tid] = {"title": title, "text": "", "done": False}
        return redirect(f"/topics/{tid}")
    return render_template("topic_new.html")

@app.route("/topics/<tid>/delete", methods=["POST"])
@login_required
def topic_delete(tid):
    user_data = get_user_data(current_user.id)
    if tid in user_data["topics"] and tid.startswith("custom_"):
        del user_data["topics"][tid]
    return jsonify({"status": "ok"})

# ─── ЭКЗАМЕН ───

@app.route("/exam")
@login_required
def exam_page():
    user_data = get_user_data(current_user.id)
    all_topics = list(FIXED_TOPICS)
    for tid, data in user_data["topics"].items():
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
    user_data = get_user_data(current_user.id)
    data = request.json
    text = data["text"].strip()
    tid = session.get("exam_topic")
    if not tid:
        return jsonify({"status": "error"})
    topic_info = next((t for t in FIXED_TOPICS if t["id"] == tid), None)
    title = topic_info["title"] if topic_info else user_data["topics"].get(tid, {}).get("title", "Своя тема")
    exam_id = str(int(time.time()))
    user_data["exams"][exam_id] = {
        "topic_id": tid,
        "title": title,
        "text": text,
        "date": str(date.today()),
        "word_count": len(text.split())
    }
    return jsonify({"status": "ok", "exam_id": exam_id})

@app.route("/exam/history")
@login_required
def exam_history():
    user_data = get_user_data(current_user.id)
    exams_list = []
    for eid, data in sorted(user_data["exams"].items(), key=lambda x: x[0], reverse=True):
        exams_list.append({
            "id": eid,
            "title": data["title"],
            "date": data["date"],
            "word_count": data["word_count"]
        })
    return render_template("exam_history.html", exams=exams_list)

# ─── ПЕРЕВОДЧИК ───

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

# ─── FAQ ───

@app.route("/faq")
def faq_page():
    return render_template("faq.html")

# ─── УЧЁБА ───

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
    if not IRREGULAR_VERBS:
        return render_template("irregular_train.html", empty=True)
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
@login_required
def games_page():
    return render_template("games.html")

@app.route("/games/hangman")
@login_required
def hangman_page():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 4 <= len(w) <= 12 and " " not in w]
    if not available:
        return render_template("hangman.html", empty=True)
    word = random.choice(available).lower()
    section_id = all_w[word]["section"]
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
@login_required
def quiz_page():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 4 <= len(w) <= 12 and " " not in w]
    if len(available) < 4:
        return render_template("quiz.html", empty=True)
    session["quiz_score"] = 0
    session["quiz_question"] = 0
    session["quiz_total"] = 10
    session["quiz_used"] = []
    session["quiz_errors"] = []
    return render_template("quiz.html", empty=False)

@app.route("/games/quiz/question")
@login_required
def quiz_question():
    all_w = get_all_words(current_user.id)
    available = [w for w in all_w.keys() if 4 <= len(w) <= 12 and " " not in w and w not in session.get("quiz_used", [])]
    if not available:
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

    return jsonify({
        "status": "ok",
        "word": word,
        "options": options,
        "correct": correct,
        "question_num": question_num,
        "total": session.get("quiz_total", 10)
    })

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

    return jsonify({
        "status": "ok",
        "correct": is_correct,
        "correct_answer": correct,
        "score": session.get("quiz_score", 0)
    })

@app.route("/games/quiz/result")
@login_required
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
    word = speed_words[index]
    return jsonify({
        "status": "ok",
        "word": word,
        "index": index + 1,
        "total": len(speed_words)
    })

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
    return jsonify({
        "status": "ok",
        "correct": is_correct,
        "correct_answer": all_w[word]["rus"],
        "score": session.get("speed_score", 0),
        "index": index + 1,
        "total": len(speed_words)
    })

@app.route("/games/speed/result")
@login_required
def speed_result():
    return jsonify({
        "score": session.get("speed_score", 0),
        "total": len(session.get("speed_words", []))
    })

# ─── УТИЛИТЫ ───

@app.route("/utils")
@login_required
def utils_page():
    return render_template("utils.html")

@app.route("/export/words")
@login_required
def export_words():
    user_data = get_user_data(current_user.id)
    all_w = get_all_words(current_user.id)
    text = "МОИ СЛОВА\n\n"
    for eng, data in all_w.items():
        section = get_section(data["section"])
        text += f"{eng} - {data['rus']} ({section['title']})\n"
    return Response(
        text,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=my_words.txt"}
    )

@app.route("/export/phrases")
@login_required
def export_phrases():
    user_data = get_user_data(current_user.id)
    text = "МОИ ФРАЗЫ\n\n"
    for eng, rus in user_data["phrases"].items():
        text += f"{eng} - {rus}\n"
    return Response(
        text,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=my_phrases.txt"}
    )

@app.route("/export/section/<sid>")
@login_required
def export_section(sid):
    user_data = get_user_data(current_user.id)
    section = get_section(sid)
    if sid == "general":
        words_to_export = user_data["general_words"]
    else:
        words_to_export = {k: v for k, v in common_words.items() if v.get("section") == sid}
    text = f"КАТЕГОРИЯ: {section['title'].upper()}\n\n"
    for eng, data in words_to_export.items():
        text += f"{eng} - {data['rus']}\n"
    return Response(
        text,
        mimetype="text/plain",
        headers={"Content-Disposition": f"attachment; filename={sid}.txt"}
    )

@app.route("/export/topics")
@login_required
def export_topics():
    user_data = get_user_data(current_user.id)
    text = "МОИ ТОПИКИ\n\n"
    for tid, data in user_data["topics"].items():
        if data.get("done"):
            text += f"=== {data.get('title', 'Без названия')} ===\n"
            text += data.get("text", "") + "\n\n"
    return Response(
        text,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=my_topics.txt"}
    )

# ─── АВТОРИЗАЦИЯ ───

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
        
        new_code = EmailCode(email=email, code=code)
        db.session.add(new_code)
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

@app.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
