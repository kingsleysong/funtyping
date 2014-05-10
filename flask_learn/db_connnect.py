from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root@localhost/funtyping'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), unique=True)
    code = db.Column(db.String(100))
    user_query = db.relationship('UserInfo',backref='userq')
   
    def __init__(self, username, password, code):
        self.username = username
        self.password = password
        self.code = code

    def __repr__(self):
        return '<User %r>' % self.username

'''
# db.create_all()
admin = User("shq","123","fjdkafjdlksfjlkdsjfds")
db.session.add(admin)
db.session.commit()
users = User.query.all()
print users

'''
class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __init__(self, userid):
        self.userid = userid
#db.create_all()

uq = UserInfo(1)
#user = User("shq","123","fdsafdsafdsaf")
#db.session.add(uq)
#db.session.commit()
print ', '.join(['%s:%s' % item for item in uq.userq.__dict__.items()])
print uq.userq
