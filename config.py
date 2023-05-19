
import os
from os import path
import pymysql
pymysql.install_as_MySQLdb()
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(path.join(basedir, ".flaskenv"))


class Config(object):
    """To make configurations more flexible and safe, most settings can be optionally imported from environment variables"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <texdata.analytic@gmail.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "RedisCache",  # caching type
    CACHE_DEFAULT_TIMEOUT = 3600  # dafault cache time
    CACHE_REDIS_HOST = "127.0.0.1"
    CACHE_REDIS_PORT = 3000


    @staticmethod
    def init_app(app):
        pass

# The SQLALCHEMY_DATABASE_URI variable is assigned different values under each of the three configurations below:
# This is very important, as you don’t want a run of the unit tests to change the database that you use for day-to-day development.
# Each configuration tries to import the database URL from an environment variable, and when that is not
# ...available it sets a default one based on SQLite. For the testing configuration, the
# ...default is an in-memory database, since there is no need to store any data outside of the test run.
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# The different configurations are then registered in a config dictionary. The development configuration is also
# ...registered as the default
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
