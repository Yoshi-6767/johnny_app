from flask import Blueprint, render_template, session
from flask_login import login_required, current_user
from jp_data import HIRAGANA, JP_WORDS
from ja_l0 import JA_L0_U1, JA_L0_U2
from ja_hiragana import ALL_HIRAGANA_UNITS  # Импортируем наши новые данные

jp_bp = Blueprint('jp', __name__, url_prefix='/jp', template_folder='jp_app/templates')

# ... (тут остаются старые роуты для /jp, /friends, /words)

@jp_bp.route('/hiragana')
@login_required
def jp_hiragana():
    # Передаем карту юнитов (Уроки + Экзамен)
    return render_template('jp_hiragana.html', units=ALL_HIRAGANA_UNITS)

@jp_bp.route('/hiragana/lesson/<unit_id>')
@login_required
def jp_hiragana_lesson(unit_id):
    # Ищем юнит по ID
    unit = next((u for u in ALL_HIRAGANA_UNITS if u["id"] == unit_id), None)
    if not unit:
        return "Урок не найден", 404
    
    return render_template('jp_lesson.html', unit=unit, user=current_user)

# ... (роут для старых уроков /jp/lesson/<unit_id> оставляем, если нужен)
