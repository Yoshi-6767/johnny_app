import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "flow_and_word_dev_fallback_key_change_me")
    
    SQLALCHEMY_DATABASE_URI = "sqlite:////data/users.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    AVATAR_FOLDER = "/data/avatars"
    
    SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.yandex.ru")
    SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
    SMTP_USER = os.environ.get("SMTP_USER", "")
    SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", "")

    # Порог для автоматической пометки слова как «выучено»
    LEARNED_THRESHOLD = 3
