# -*- coding:utf-8 -*-

from funtyping.utils.mail import check_email_name
from funtyping.models.user_model import User, UserRegist
class FormMessage():
    def __init__(self, is_success, message=''):
        self.is_success = is_success
        self.message = message

class RegistForm():
    def __init__(self, email):
        self.email = email
    def validate(self):
        if self.email == '':
            return FormMessage(False, u'邮件不能为空')
        if not check_email_name(self.email):
            return FormMessage(False, u'请输入合法的邮件地址')
        return FormMessage(True)

class RegistPasswordForm():
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def validate(self):
        if self.email == '':
            return ValidateInfo(False, u'邮箱不能为空')
        if not check_email(self.email):
            return ValidateInfo(False, u'请输入合法的邮箱地址')
        user = User.user_query.get_by_email(self.email)
        if user:
            return ValidateInfo(False, u'该邮箱已经被注册')
        return ValidateInfo(True)
