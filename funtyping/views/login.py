# -*- coding:utf-8 -*-

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
                    previous_page = request.args.get('prev')
                    if previous_page:
                        return redirect(previous_page)
                    return redirect(url_for('latest'))
                else:
                    flash(u'用户名或密码错误')
        else:
            flash(result.message)
    return render_template('login.html', email=email)
