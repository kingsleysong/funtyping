#-*- coding:utf-8 -*-
from funtyping import app
from flask import render_template
@app.route('/regist',methods=['POST','GET'])
def regist():
	return render_template('regist.html')
@app.route('/welcome',methods=['POST','GET'])
def welcome():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        email = request.form['email'].strip()
        email_is_valid = RegistForm(email=email).validate()
        if email_is_valid.is_success:
            user = User.user_query.get_by_email(email)
            if user:
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
    if request.method == 'GET'
        return render_template('password.html')
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        result = RegistPasswordForm(email=email, password=password).validate()
        if result.is_success:
            user = User.create(email=email, password=password, status=USER_STATUS_INVALID)
            return render_template('write.html')
        else:
            return render_template('password.html')
