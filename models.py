from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    avatar = db.Column(db.String(200), default=None)


class EmailCode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class LearnedWord(db.Model):
    """Слово, которое юзер выучил (3 правильных подряд ИЛИ вручную)."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    section = db.Column(db.String(50), nullable=False)
    learned_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'word', name='_user_word_uc'),
    )


class WordProgress(db.Model):
    """Счётчик правильных подряд по каждому слову."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    correct_streak = db.Column(db.Integer, default=0)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'word', name='_user_word_progress_uc'),
    )


class SectionExam(db.Model):
    """Попытка экзамена по категории."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    section_id = db.Column(db.String(50), nullable=False)
    is_passed = db.Column(db.Boolean, default=False)
    total_questions = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    errors_json = db.Column(db.Text, default="[]")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Achievement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    unlocked_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'code', name='_user_achievement_uc'),
    )


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    goal_type = db.Column(db.String(20), nullable=False)
    target = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)


# ═══ НОВЫЕ МОДЕЛИ ДЛЯ ПЕРЕНОСА В БД ═══

class UserWord(db.Model):
    """Свои слова юзера (категория general)."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    eng = db.Column(db.String(200), nullable=False)
    rus = db.Column(db.String(200), nullable=False)
    section = db.Column(db.String(50), default='general')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'eng', name='_user_word_eng_uc'),
    )


class UserPhrase(db.Model):
    """Свои фразы юзера."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    eng = db.Column(db.String(300), nullable=False)
    rus = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'eng', name='_user_phrase_eng_uc'),
    )


class UserTopic(db.Model):
    """Топики юзера: фикс (id типа 'my_day') и кастомные ('custom_...')."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    topic_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, default='')
    is_done = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'topic_id', name='_user_topic_uc'),
    )


class UserExam(db.Model):
    """Экзамены-тексты юзера."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exam_id = db.Column(db.String(50), nullable=False)
    topic_id = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, default='')
    word_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'exam_id', name='_user_exam_uc'),
    )


class UserProgress(db.Model):
    """Прогресс юзера. Одна запись на юзера. History и weak_words — JSON-строки."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, unique=True)
    streak = db.Column(db.Integer, default=0)
    last_day = db.Column(db.String(20), default='')
    history_json = db.Column(db.Text, default='[]')
    weak_words_json = db.Column(db.Text, default='{}')
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
