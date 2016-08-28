# -*- coding:utf-8 -*-
import os
# falsk 模板渲染 会话 重定向 从修饰器生成url
from flask import Flask, render_template, session, redirect, url_for
# 命令行工具
from flask.ext.script import Manager, Shell
# 模板
from flask.ext.bootstrap import Bootstrap
# 时间
from flask.ext.moment import Moment
# 表单
from flask.ext.wtf import Form
# 字符串表单 提交按钮
from wtforms import StringField, SubmitField
# 验证提交的表单是否为空
from wtforms.validators import Required
# 数据库
from flask.ext.sqlalchemy import SQLAlchemy
# 数据库迁移
from flask.ext.migrate import Migrate, MigrateCommand

# 得到当前绝对地址
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 密钥
app.config['SECRET_KEY'] = 'hard to guess string'
# 数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] =('mysql://root:306235911@localhost/xian')
# 每次结束会话前提交
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# 初始化命令行 模板 时间 数据库 数据库迁移模块 邮箱模块
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# 
# 
# 
# 数据库模型role
class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    detal = db.Column(db.String(140))
    # 以后可尝试使用外键
    img1 = db.Column(db.String(70))
    img2 = db.Column(db.String(70))
    img3 = db.Column(db.String(70))

    def __repr__(self):
        return '<Item %r>' % self.name




# # 输入姓名的表单
# class NameForm(Form):
#     name = StringField('What is your name?', validators=[Required()])
#     submit = SubmitField('Submit')


# 404错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# 500错误处理
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# 主页面
@app.route('/', methods=['GET', 'POST'])
def index():
    items = Item.query.all()
    return render_template('myindex.html', items = items)
    # return render_template('oneitem.html')
# 
# @app.route('/item/<itemName>')
# def item(itemName):
#     item = Item.query.filter_by(itemName = itemName).first()
#     return render_template('item.html' , itemName = itemName)


if __name__ == '__main__':
    manager.run()
