import os

class Config(object):
    SECRET_KEY = 'bwt35sQ'
    SQLALCHEMY_DATABASE_URI = 'postgresql://taskrole:taskrole77@localhost:5432/task'
    SQLALCHEMY_TRACK_MODIFICATIONS = False