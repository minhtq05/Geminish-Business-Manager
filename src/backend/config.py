from decouple import config

DATABASE_URI = config('DATABASE_URL')


class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
