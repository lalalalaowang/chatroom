from wtforms import Form
from wtforms.fields import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email, Regexp, Length, ValidationError
from app.models.crud import Crud


class RegistForm(Form):
    name = StringField('昵称', validators=[DataRequired('昵称不能为空')])
    pwd = PasswordField('密码', validators=[DataRequired('密码不能为空'),
                                          Length(min=6, message='密码长度不能小于6位', )])
    repwd = PasswordField('确认密码', validators=[DataRequired('确认密码不能为空'),
                                              EqualTo('pwd', message='两次输入的密码不一致')])
    email = StringField('邮箱', validators=[DataRequired('邮箱不能为空'), Email('邮箱格式不正确')])
    phone = StringField('手机', validators=[DataRequired('手机不能为空'),
                                          Regexp('1[345789]\\d{9}', message='手机格式不正确')])

    def validate_name(self, field):
        if Crud.user_unique(field.data):
            raise ValidationError('昵称已经存在')

    def validate_email(self, field):
        if Crud.user_unique(field.data):
            raise ValidationError('邮箱已经存在')

    def validate_phone(self, field):
        if Crud.user_unique(field.data):
            raise ValidationError('手机已经存在')
