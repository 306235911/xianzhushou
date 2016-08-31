# -*- coding:utf8 -*-
from flask_wtf import Form
from wtforms import StringField, TextAreaField, BooleanField, SelectField,\
    SubmitField
from wtforms.validators import Required, Length, Email, Regexp
from wtforms import ValidationError
from ..models import Role, User


class NameForm(Form):
    name = StringField(u'你的名字', validators=[Required()])
    submit = SubmitField(u'提交')


class EditProfileForm(Form):
    name = StringField(u'真实姓名', validators=[Length(0, 64)])
    location = StringField(u'所在宿舍栋数及宿舍号', validators=[Length(0, 64)])
    tel = StringField(u'电话号码',  validators=[Length(0, 64)])
    submit = SubmitField(u'提交')


class EditProfileAdminForm(Form):
    email = StringField(u'电子邮件', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField(u'用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z\u4e00-\u9fa5][a-zA-Z0-9_\u4e00-\u9fa5]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    confirmed = BooleanField(u'确认')
    role = SelectField(u'角色', coerce=int)
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    tel = StringField(u'电话号码',  validators=[Length(0, 64)])
    submit = SubmitField(u'提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError(u'邮箱已验证')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError(u'用户名已被使用')
