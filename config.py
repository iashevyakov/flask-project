import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = os.environ.get('REDIS_HOST')
    REDIS_PORT = '6379'
    REDIS_DB = 0