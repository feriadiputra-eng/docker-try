import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DB_HOST = os.environ.get("DB_HOST")
    DB_DATABASE = os.environ.get("DB_DATABASE")
    DB_USERNAME = os.environ.get("DB_USERNAME")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + username + ':' + password + '@' + '/' + database
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True