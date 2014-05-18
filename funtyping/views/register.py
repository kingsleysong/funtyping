#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template,request,flash,redirect,url_for
from funtyping.forms import regist_form 
from funtyping.models.user_model import User,UserRegist 
from funtyping.utils.mail import send_regist_mail
from funtyping.utils.consts import USER_STATUS_INVALID,USER_STATUS_NORMAL
import random
@app.route('/regist',methods=['POST','GET'])
@app.route('/')
def regist():
	return render_template('regist.html')
@app.route('/welcome',methods=['POST','GET'])
def welcome():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        email = request.form['email'].strip()
        email_is_valid = regist_form.RegistForm(email=email).validate()
        if email_is_valid.is_success:
            user = UserRegist.user_regist_query.get_by_email(email)
            if user != None:
                flash(u'该邮件已经注册')
            else:
                code = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz1234567890',20))
                regist_result = send_regist_mail(email, code)
                if regist_result:
                    UserRegist.create(email, code)
                    return render_template('password.html',email=email)
                else:
                    flash(u'发送失败，请重试')
        else:
            flash(email_is_valid.message)

        return redirect(url_for('regist'))
@app.route('/init-user')
def init_user():
    email = request.args.get('email')
    code = request.args.get('code')
    r_user = UserRegist.user_query.get_by_email(email)
    if not r_user:
        flash(u'该邮箱已经注册')
        return redirect(url_for('regist'))
    is_valid = r_user.check(r_user.code)
    if not is_valid:
        flash(u'该邮箱已经注册')
        return redirect(url_for('register'))
    user = User.user_query.get_by_email(email)
    user.set_status(USER_STATUS_NORMAL)
    return "latest notes"

@app.route('/init-password', methods=['GET','POST'])
def init_password():
    if request.method == 'GET':
        return render_template('password.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = regist_form.RegistPasswordForm(email=email, password=password).validate()
        if result.is_success:
            user = User.create(email=email, password=password, status=USER_STATUS_INVALID)
            return render_template('write.html')
        else:
            return render_template('password.html')
