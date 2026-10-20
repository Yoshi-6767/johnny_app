from flask import Blueprint, render_template, session
from jp_data import HIRAGANA, JP_WORDS
from flask_login import login_required, current_user

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
