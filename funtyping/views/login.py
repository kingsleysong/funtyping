# -*- coding:utf-8 -*-

from funtyping import app
from flask import request, flash , render_template, redirect, session, url_for
from funtyping.utils.util import get_user_id
from funtyping.forms.login_form import LoginForm
from funtyping.forms.change_password_form import ChangePasswordForm
from funtyping.models.user_model import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        user_id = get_user_id()
        if user_id: 
            return redirect(url_for('latest'))
        return render_template('login.html')
    elif request.method == 'POST':
        email = request.form['email'].strip()
        password = request.form['password'].strip()
        result = LoginForm(email=email, password=password).validate()
        if result.is_success:
            user = User.user_query.get_by_email(email)
            if user is None:
                flash(u'该邮件尚未注册')
            else:
                result = user.check(password)
                if result:
                    session["user_id"] = user.id
                    previous_page = request.args.get('prev')
                    if previous_page:
                        return redirect(previous_page)
                    return redirect(url_for('latest'))
                else:
                    flash(u'用户名或密码错误')
        else:
            flash(result.message)
    return render_template('login.html', email=email)

@app.route('/logout')
def logout():
    if "user_id" in session:
        del session["user_id"]
    return redirect(url_for('regist'))

@app.route('/setting/password',methods=['GET','POST'])
def change_password():
    if request.method == 'GET':
        return render_template('change_password.html')
    if request.method == 'POST':
        user_id = get_user_id()
        old_password = request.form['old']
        new_password = request.form['new']
        confirm_password = request.form['confirm']
        result = ChangePasswordForm(new_password,confirm_password).validate()
        if result.is_success:
            user = User.user_query.get_by_id(user_id)
            result = user.check(old_password)
            if result:
                user.set_password(new_password)
                flash(u'密码已修改')
            else:
                flash(u'原密码输入错误')
        else:
            flash(result.message)
        return render_template('change_password.html')
