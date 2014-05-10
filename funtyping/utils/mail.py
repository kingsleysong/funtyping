# -*- coding:utf-8 -*-

import re
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from funtyping.app_config import MAIL_HOST, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD

def send_regist_mail(mail_to , code):
    def __generate_regist_url():
        f = open('funtyping/utils/regist_mail.tpl','r')
        body = f.read()
        base_url = 'http://117.121.10.71:5000/init-user?email=%s&code=%s'
        body_url = base_url %(mail_to, code)
        return body.format(body_url)
    try:
        title = '欢迎注册funtyping'
        body = __generate_regist_url()
        send_mail(mail_to, title, body)
        return True
    except:
        return False
def send_mail(mail_to, title, text):
    # 构造邮件消息格式
    message = MIMEMultipart('alternative')
    message['From'] = MAIL_USERNAME
    message['To'] = mail_to
    message['Subject'] = title
    text = MIMEText(text, 'html')
    message.attach(text)
    # 连接到服务器 
    mail_server = smtplib.SMTP(MAIL_HOST)
    # 返回服务器的特性
    code = mail_server.ehlo()[0]
    if not (200 <= code <= 299):
        raise SMTPHeloError(code)
    # 登录到邮件服务器
    print MAIL_USERNAME
    print MAIL_PASSWORD
    mail_server.login(MAIL_USERNAME, MAIL_PASSWORD)
    # 发送邮件
    mail_server.sendmail(MAIL_USERNAME, mail_to, message.as_string())
    # 退出
    mail_server.quit()
def check_email_name(email_name):
    return re.match("(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)", email_name)
