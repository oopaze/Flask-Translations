import os


class BaseSettings:
    SECRET_KEY = "5n)5wm0-u7v2us+)bdg*g@_%_8e&xw5otvh&u&du_z87%(4+)+"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class Development(BaseSettings):
    DEBUG = True
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
    ENV = 'development'
