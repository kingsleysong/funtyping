# -*- coding:utf-8 -*-
from funtyping.forms.regist_form import FormMessage
class LoginForm():

    def __init__(self, email, password, username=''):
        self.email = email
        self.password = password
        self.username = username

    def validate(self):
        if self.email == '':
            return FormMessage(False, u'邮箱不能为空')
        if self.password == '':
            return FormMessage(False, u'密码不能为空')
        return FormMessage(True)

