from datetime import datetime
from models import db, Achievement


# ═══════════════════════════════════════════════
# СПИСОК АЧИВОК
# ═══════════════════════════════════════════════
# category: streak / words / learned / exams / games / study / topics / phrases / special
# tier: bronze / silver / gold

ACHIEVEMENTS = [
    # 🔥 СТРИК
    {"code": "streak_1",   "title": "Первый шаг",        "desc": "Заходил 1 день", "emoji": "🌱", "category": "streak", "tier": "bronze"},
    {"code": "streak_3",   "title": "Разогрев",          "desc": "3 дня подряд",  "emoji": "🔥", "category": "streak", "tier": "bronze"},
    {"code": "streak_7",   "title": "Неделя огня",       "desc": "7 дней подряд",  "emoji": "⚡", "category": "streak", "tier": "silver"},
    {"code": "streak_14",  "title": "Две недели",        "desc": "14 дней подряд", "emoji": "💪", "category": "streak", "tier": "silver"},
    {"code": "streak_30",  "title": "Месяц дисциплины",  "desc": "30 дней подряд", "emoji": "👑", "category": "streak", "tier": "gold"},

    # 📚 СВОИ СЛОВА
    {"code": "words_1",    "title": "Первое слово",      "desc": "Добавил 1 своё слово", "emoji": "✍️", "category": "words", "tier": "bronze"},
    {"code": "words_10",   "title": "Десятка",           "desc": "Добавил 10 своих слов", "emoji": "📖", "category": "words", "tier": "bronze"},
    {"code": "words_50",   "title": "Полтинник",         "desc": "Добавил 50 своих слов", "emoji": "📚", "category": "words", "tier": "silver"},
    {"code": "words_100",  "title": "Сотка",             "desc": "Добавил 100 своих слов", "emoji": "🎯", "category": "words", "tier": "gold"},

    # 🧠 ВЫУЧЕНО (learned)
    {"code": "learned_10",  "title": "Первые 10",        "desc": "Выучил 10 слов", "emoji": "💯", "category": "learned", "tier": "bronze"},
    {"code": "learned_50",  "title": "Пятьдесят",        "desc": "Выучил 50 слов", "emoji": "🧠", "category": "learned", "tier": "silver"},
    {"code": "learned_100", "title": "Сто выучено",      "desc": "Выучил 100 слов", "emoji": "🎓", "category": "learned", "tier": "gold"},

    # 🎓 ЭКЗАМЕНЫ ПО КАТЕГОРИЯМ
    {"code": "exam_1",   "title": "Первый экзамен",      "desc": "Сдал 1 категорию", "emoji": "🎓", "category": "exams", "tier": "bronze"},
    {"code": "exam_5",   "title": "Пятёрка",             "desc": "Сдал 5 категорий", "emoji": "🏅", "category": "exams", "tier": "silver"},
    {"code": "exam_10",  "title": "Десятка экзаменов",   "desc": "Сдал 10 категорий", "emoji": "👑", "category": "exams", "tier": "gold"},

    # 🎮 ИГРЫ
    {"code": "game_hangman_win",     "title": "Палач",         "desc": "Выиграл в Виселицу", "emoji": "🪢", "category": "games", "tier": "bronze"},
    {"code": "game_quiz_10",         "title": "Знаток",        "desc": "10/10 в Квизе", "emoji": "❓", "category": "games", "tier": "silver"},
    {"code": "game_speed_10",        "title": "Скоростной",    "desc": "10/10 в Скоростном", "emoji": "⚡", "category": "games", "tier": "silver"},
    {"code": "game_listening_10",    "title": "Слухач",        "desc": "10/10 в Аудио-квизе", "emoji": "🎧", "category": "games", "tier": "silver"},
    {"code": "game_emoji_10",        "title": "Эмодзи-мастер", "desc": "10/10 в Эмодзи-квизе", "emoji": "🍎", "category": "games", "tier": "silver"},
    {"code": "game_odd_one_10",      "title": "Детектив",      "desc": "10/10 в «Что лишнее»", "emoji": "🎯", "category": "games", "tier": "silver"},
    {"code": "game_millionaire_10",  "title": "Миллионер",     "desc": "10+ в Миллионере", "emoji": "💰", "category": "games", "tier": "gold"},

    # 📖 УЧЁБА
    {"code": "study_irregular",  "title": "Знаток глаголов", "desc": "20+ правильных в глаголах", "emoji": "🔤", "category": "study", "tier": "silver"},
    {"code": "study_all",        "title": "Книжный червь",   "desc": "Открыл все 3 раздела учёбы", "emoji": "📚", "category": "study", "tier": "bronze"},

    # 📝 ТОПИКИ
    {"code": "topic_1",    "title": "Первый топик",       "desc": "Написал 1 топик", "emoji": "✏️", "category": "topics", "tier": "bronze"},
    {"code": "topic_5",    "title": "Пять топиков",       "desc": "Написал 5 топиков", "emoji": "📝", "category": "topics", "tier": "silver"},
    {"code": "topic_10",   "title": "Десять топиков",     "desc": "Написал 10 топиков", "emoji": "✍️", "category": "topics", "tier": "gold"},
    {"code": "exam_text_1","title": "Письменный экзамен", "desc": "Сдал первый экзамен-текст", "emoji": "🎓", "category": "topics", "tier": "bronze"},

    # 💬 ФРАЗЫ
    {"code": "phrase_1",   "title": "Первая фраза",       "desc": "Добавил 1 фразу", "emoji": "💬", "category": "phrases", "tier": "bronze"},
    {"code": "phrase_10",  "title": "Десятка фраз",       "desc": "Добавил 10 фраз", "emoji": "🗣️", "category": "phrases", "tier": "silver"},

    # 🌟 ОСОБЫЕ
    {"code": "special_sniper",  "title": "Снайпер",       "desc": "20 правильных подряд без ошибок", "emoji": "🎯", "category": "special", "tier": "gold"},
    {"code": "special_early",   "title": "Ранняя пташка", "desc": "Зашёл до 7 утра", "emoji": "⏰", "category": "special", "tier": "bronze"},
]


# ═══════════════════════════════════════════════
# ХЕЛПЕРЫ
# ═══════════════════════════════════════════════

def get_achievement(code):
    return next((a for a in ACHIEVEMENTS if a["code"] == code), None)


def get_unlocked_codes(user_id):
    rows = Achievement.query.filter_by(user_id=user_id).all()
    return {r.code for r in rows}


def unlock(user_id, code):
    """Открывает ачивку, если ещё не открыта.
       Возвращает True, если только что открыли."""
    exists = Achievement.query.filter_by(user_id=user_id, code=code).first()
    if exists:
        return False
    db.session.add(Achievement(user_id=user_id, code=code))
    return True


# ═══════════════════════════════════════════════
# ПРОВЕРКИ
# ═══════════════════════════════════════════════

def check_all(user_id, progress, general_words_count, phrases_count, topics_done,
              exams_count, learned_count, games_stats, study_stats):
    """Проверяет все ачивки и возвращает список новых кодов."""
    newly = []

    # СТРИК
    streak = progress.get("streak", 0)
    if streak >= 1 and unlock(user_id, "streak_1"):     newly.append("streak_1")
    if streak >= 3 and unlock(user_id, "streak_3"):     newly.append("streak_3")
    if streak >= 7 and unlock(user_id, "streak_7"):     newly.append("streak_7")
    if streak >= 14 and unlock(user_id, "streak_14"):   newly.append("streak_14")
    if streak >= 30 and unlock(user_id, "streak_30"):   newly.append("streak_30")

    # СВОИ СЛОВА
    if general_words_count >= 1 and unlock(user_id, "words_1"):       newly.append("words_1")
    if general_words_count >= 10 and unlock(user_id, "words_10"):     newly.append("words_10")
    if general_words_count >= 50 and unlock(user_id, "words_50"):     newly.append("words_50")
    if general_words_count >= 100 and unlock(user_id, "words_100"):   newly.append("words_100")

    # LEARNED
    if learned_count >= 10 and unlock(user_id, "learned_10"):   newly.append("learned_10")
    if learned_count >= 50 and unlock(user_id, "learned_50"):   newly.append("learned_50")
    if learned_count >= 100 and unlock(user_id, "learned_100"): newly.append("learned_100")

    # ЭКЗАМЕНЫ
    if exams_count >= 1 and unlock(user_id, "exam_1"):   newly.append("exam_1")
    if exams_count >= 5 and unlock(user_id, "exam_5"):   newly.append("exam_5")
    if exams_count >= 10 and unlock(user_id, "exam_10"): newly.append("exam_10")

    # ИГРЫ
    if games_stats.get("hangman_win") and unlock(user_id, "game_hangman_win"):           newly.append("game_hangman_win")
    if games_stats.get("quiz_10") and unlock(user_id, "game_quiz_10"):                   newly.append("game_quiz_10")
    if games_stats.get("speed_10") and unlock(user_id, "game_speed_10"):                 newly.append("game_speed_10")
    if games_stats.get("listening_10") and unlock(user_id, "game_listening_10"):         newly.append("game_listening_10")
    if games_stats.get("emoji_10") and unlock(user_id, "game_emoji_10"):                 newly.append("game_emoji_10")
    if games_stats.get("odd_one_10") and unlock(user_id, "game_odd_one_10"):             newly.append("game_odd_one_10")
    if games_stats.get("millionaire_10") and unlock(user_id, "game_millionaire_10"):     newly.append("game_millionaire_10")

    # УЧЁБА
    if study_stats.get("irregular_score", 0) >= 20 and unlock(user_id, "study_irregular"): newly.append("study_irregular")
    if study_stats.get("all_sections_visited") and unlock(user_id, "study_all"):          newly.append("study_all")

    # ТОПИКИ
    if topics_done >= 1 and unlock(user_id, "topic_1"):   newly.append("topic_1")
    if topics_done >= 5 and unlock(user_id, "topic_5"):   newly.append("topic_5")
    if topics_done >= 10 and unlock(user_id, "topic_10"): newly.append("topic_10")

    # ФРАЗЫ
    if phrases_count >= 1 and unlock(user_id, "phrase_1"):   newly.append("phrase_1")
    if phrases_count >= 10 and unlock(user_id, "phrase_10"): newly.append("phrase_10")

    # ОСОБЫЕ
    if progress.get("correct_streak_global", 0) >= 20 and unlock(user_id, "special_sniper"):
        newly.append("special_sniper")
    if datetime.now().hour < 7 and unlock(user_id, "special_early"):
        newly.append("special_early")

    db.session.commit()
    return newly
