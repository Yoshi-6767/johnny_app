from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from jp_data import HIRAGANA, JP_WORDS
from ja_l0 import JA_L0_U1, JA_L0_U2

# Список всех доступных уроков
ALL_LESSONS = [
    {"id": JA_L0_U1["id"], "title": JA_L0_U1["title"]["ru"], "level": JA_L0_U1["level"], "order": JA_L0_U1["order"]},
    {"id": JA_L0_U2["id"], "title": JA_L0_U2["title"]["ru"], "level": JA_L0_U2["level"], "order": JA_L0_U2["order"]},
]

jp_bp = Blueprint('jp', __name__, url_prefix='/jp', template_folder='jp_app/templates')

@jp_bp.route('/')
@login_required
def jp_index():
    stats = {
        "streak": 0,
        "words_learned": 0,
        "lessons_done": 0
    }
    sections = [
        {"title": "Азбука (Хирагана)", "desc": "Учим японские буквы", "icon": "あ", "link": "/jp/hiragana"},
        {"title": "Слова (Кандзи)", "desc": "Иероглифы и их чтение", "icon": "漢", "link": "/jp/words"},
        {"title": "Грамматика", "desc": "Структура предложений", "icon": "文", "link": "#"},
        {"title": "Тренировка", "desc": "Повторение слов", "icon": "🔁", "link": "#"},
    ]
    return render_template('jp_index.html', user=current_user, lessons=ALL_LESSONS, stats=stats, sections=sections)

@jp_bp.route('/hiragana')
@login_required
def jp_hiragana():
    return render_template('jp_hiragana.html', hiragana=HIRAGANA)

@jp_bp.route('/words')
@login_required
def jp_words():
    return render_template('jp_words.html', words=JP_WORDS)

@jp_bp.route('/friends')
@login_required
def jp_friends():
    return render_template('jp_friends.html')

# ВОТ ЭТОТ РОУТ ОТВЕЧАЕТ ЗА УРОКИ
@jp_bp.route('/lesson/<unit_id>')
@login_required
def jp_lesson(unit_id):
    if unit_id == JA_L0_U1["id"]:
        unit = JA_L0_U1
    elif unit_id == JA_L0_U2["id"]:
        unit = JA_L0_U2
    else:
        return "Урок не найден", 404
    
    return render_template('jp_lesson.html', unit=unit, user=current_user)
