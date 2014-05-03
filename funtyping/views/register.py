from funtyping import app
from flask import render_template
@app.route('/regist',methods=['POST','GET'])
def regist():
	return render_template('regist.html')


def get_user_id():
	return 0
