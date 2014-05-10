from flask import Flask,url_for,request,render_template,make_response,escape,sessions

app = Flask("Funtyping")

@app.route('/hello/<name>')
def hello_world(name):
     return render_template('hello.html',name=name)
@app.route("/index/")
def index():
    return render_template('login.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
	if len(request.form["username"]) < 8 or len(request.form["password"]) < 8 :
	     error = "username or password is invalid"
        else:
             error = "login success, please access other pages"
    else:
	return "error not support get request"

    return render_template('login_result.html',error = error)
@app.route('/send_cookie',methods=['GET','POST'])
def send_cookie():
    resp = make_response(render_template('login.html'))
    resp.set_cookie('username','kingsley')
    return resp
@app.route('/recv_cookie',methods=['GET','POST'])
def recv_cookie() :
    username = request.cookies.get('username')
    return username

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
