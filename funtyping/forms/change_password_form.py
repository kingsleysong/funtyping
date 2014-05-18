# -*- coding:utf-8 -*-
from funtyping.forms.regist_form import FormMessage

class ChangePasswordForm():

    def __init__(self, new_password, confirm_password):
        self.new_password = new_password
        self.confirm_password = confirm_password

    def validate(self):
        if self.new_password != self.confirm_password:
            return FormMessage(False, u'两次密码输入不一致')
        return FormMessage(True)
