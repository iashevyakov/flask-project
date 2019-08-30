import os

class Config(object):
    SECRET_KEY = 'bwt35sQ'
    SQLALCHEMY_DATABASE_URI = 'postgresql://taskrole:taskrole77@db:5432/task'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = 'redis'
    REDIS_PORT = '6379'
    REDIS_DB = 0