# -*- coding:utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.sina.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = u'闲'
    FLASKY_MAIL_SENDER = 'daxiong306235911@sina.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ('mysql://root:306235911@localhost/xian')
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = ('mysql://root:306235911@localhost/xian')
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ('mysql://root:306235911@localhost/xian')
    
config = {
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}