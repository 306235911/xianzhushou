# -*- coding:utf-8 -*-
import os
import sae.const

basedir = os.path.abspath(os.path.dirname(__file__))

dbname = sae.const.MYSQL_DB      # 数据库名
user = sae.const.MYSQL_USER    # 用户名
password = sae.const.MYSQL_PASS    # 密码
hostname = sae.const.MYSQL_HOST    # 主库域名（可读写）
port = int(sae.const.MYSQL_PORT)    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int
# sae.const.MYSQL_HOST_S  # 从库域名（只读）

url = "mysql://%s:%s@%s:%d/%s" % (user , password , hostname , port , dbname)

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
    FLASKY_POSTS_PER_PAGE = 3
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (url)
    #                                 mysql+mysqldb://scott:tiger@localhost/foo
    # SQLALCHEMY_DATABASE_URI = ('mysql+mysqldb://43noz01w30:hxkw1j5iyzy42khxw0lh0j3zkz4kkh0yy3yj0w52@localhost/app_xianzhushou')
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (url)
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = (url)
    
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
    