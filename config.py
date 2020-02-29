"""
Файл с классом конфигурации для приложения.
"""

class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://test_user:password@localhost/bubuka'
    SECRET_KEY = 'I_AM_THE_BEST:)'
