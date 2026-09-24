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
    """Слово, которое юзер выучил (3 правильных подряд) ИЛИ пометил вручную.
       Не попадается в обычной тренировке."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    section = db.Column(db.String(50), nullable=False)
    learned_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'word', name='_user_word_uc'),
    )


class WordProgress(db.Model):
    """Счётчик правильных подряд по каждому слову.
       При достижении LEARNED_THRESHOLD слово становится learned."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    word = db.Column(db.String(100), nullable=False)
    correct_streak = db.Column(db.Integer, default=0)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'word', name='_user_word_progress_uc'),
    )


class SectionExam(db.Model):
    """Попытка экзамена по категории. Одна запись = один экзамен.
       is_passed=True, если все ответы верные."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    section_id = db.Column(db.String(50), nullable=False)
    is_passed = db.Column(db.Boolean, default=False)
    total_questions = db.Column(db.Integer, default=0)
    correct_answers = db.Column(db.Integer, default=0)
    errors_json = db.Column(db.Text, default="[]")  # JSON-строка с ошибками
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Achievement(db.Model):
    """Открытая ачивка у юзера. Одна запись = одна открытая ачивка."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    code = db.Column(db.String(50), nullable=False)
    unlocked_at = db.Column(db.DateTime, default=datetime.utcnow)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'code', name='_user_achievement_uc'),
    )


class Goal(db.Model):
    """Цель юзера. Например: '100 слов', 'стрик 30 дней'."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    goal_type = db.Column(db.String(20), nullable=False)  # "words" или "streak"
    target = db.Column(db.Integer, nullable=False)
    deadline = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_completed = db.Column(db.Boolean, default=False)
    completed_at = db.Column(db.DateTime, nullable=True)
