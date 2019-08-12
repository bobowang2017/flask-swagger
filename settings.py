# -*- coding: utf-8 -*-
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'some secret words')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    HOST = '127.0.0.1'
    USERNAME = 'root'
    PASSWORD = 'root'
    PORT = '3306'
    DATABASE = 'study'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT,
                                                                                      DATABASE)
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    TESTING = True


class LocalConfig(BaseConfig):
    DEBUG = True
    HOST = '127.0.0.1'
    USERNAME = 'root'
    PASSWORD = 'root'
    PORT = '3306'
    DATABASE = 'study'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4".format(USERNAME, PASSWORD, HOST, PORT,
                                                                                      DATABASE)
    SQLALCHEMY_ECHO = True


CONFIG = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'local': LocalConfig
}
