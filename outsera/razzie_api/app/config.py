import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'movielist.csv')
    APPLICATION_ROOT = "/api"
    TESTING = False
