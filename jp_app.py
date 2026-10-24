ffrom flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from jp_data import HIRAGANA, JP_WORDS
from ja_l0 import JA_L0_U1, JA_L0_U2  # Импортируем оба юнита

# Создаем Blueprint. Все пути внутри будут начинаться с /jp
jp_bp = Blueprint('jp', __name__, url_prefix='/jp', template_folder='jp_app/templates')

@jp_bp.route('/')
@login_required
def jp_index():
    return render_template('jp_index.html', user=current_user)

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

@jp_bp.route('/lesson/<unit_id>')
@login_required
def jp_lesson(unit_id):
    # Ищем нужный юнит по ID
    if unit_id == JA_L0_U1["id"]:
        unit = JA_L0_U1
    elif unit_id == JA_L0_U2["id"]:
        unit = JA_L0_U2
    else:
        return "Урок не найден", 404
    
    return render_template('jp_lesson.html', unit=unit, user=current_user)
