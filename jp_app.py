from flask import Blueprint, render_template, session
from flask_login import login_required, current_user

# Импорты данных
from jp_data import HIRAGANA, JP_WORDS
from ja_l0 import JA_L0_U1, JA_L0_U2
from ja_hiragana import ALL_HIRAGANA_UNITS

# Создаем Blueprint
jp_bp = Blueprint('jp', __name__, url_prefix='/jp', template_folder='jp_app/templates')

# --- ГЛАВНАЯ СТРАНИЦА ЯПОНСКОГО ХАБА ---
@jp_bp.route('/')
@login_required
def jp_index():
    stats = {
        "streak": 0,
        "words_learned": 0,
        "lessons_done": 0
    }
    LEVEL_0_LESSONS = [
        {"id": JA_L0_U1["id"], "title": JA_L0_U1["title"]["ru"], "order": JA_L0_U1["order"]},
        {"id": JA_L0_U2["id"], "title": JA_L0_U2["title"]["ru"], "order": JA_L0_U2["order"]},
    ]
    return render_template('jp_index.html', user=current_user, lessons=LEVEL_0_LESSONS, stats=stats)

# --- КАРТА ХИРАГАНЫ ---
@jp_bp.route('/hiragana')
@login_required
def jp_hiragana():
    return render_template('jp_hiragana.html', units=ALL_HIRAGANA_UNITS)

# --- УРОК ХИРАГАНЫ (С ВКЛАДКАМИ) ---
@jp_bp.route('/hiragana/lesson/<unit_id>')
@login_required
def jp_hiragana_lesson(unit_id):
    unit = next((u for u in ALL_HIRAGANA_UNITS if u["id"] == unit_id), None)
    if not unit:
        return "Урок не найден", 404
    return render_template('jp_lesson.html', unit=unit, user=current_user)

# --- СТАРЫЕ УРОКИ (ОСТАВЛЯЕМ ДЛЯ СОВМЕСТИМОСТИ) ---
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

# --- ОСТАЛЬНЫЕ РАЗДЕЛЫ ---
@jp_bp.route('/words')
@login_required
def jp_words():
    return render_template('jp_words.html', words=JP_WORDS)

@jp_bp.route('/friends')
@login_required
def jp_friends():
    return render_template('jp_friends.html')
