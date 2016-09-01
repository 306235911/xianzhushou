# -*- coding:utf8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email = StringField(u'电子邮箱', validators=[Required(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'密码', validators=[Required()])
    remember_me = BooleanField(u'记住我')
    submit = SubmitField(u'登陆')

class RegistrationForm(Form):
    email = StringField(u'电子邮箱', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField(u'用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z\u4e00-\u9fa5][a-zA-Z0-9_\u4e00-\u9fa5]*$', 0,
                                          u'用户名必须是字母, '
                                          u'数字，小数点或下划线')])
    password = PasswordField(u'密码', validators=[
        Required(), EqualTo('password2', message=u'两个密码必须相等')])
    password2 = PasswordField(u'确认密码', validators=[Required()])
    submit = SubmitField(u'注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(u'Email已注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError(u'该用户名已被使用')
