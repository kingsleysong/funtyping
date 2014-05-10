import datetime

from funtyping.views import db

class BlogQuery:
    @classmethod
    def get_blog_by_author(cls, user_id):
        return Blog.query.filter(Blog.user_id == user_id).order_by('-id').all()

    @classmethod
    def get_blog_by_id(cls, id):
        return Blog.query.filter(Blog.id == id).first()

    @classmethod
    def get_datenum_by_user(cls, user_id):
        return db.session.query(Blog.update_time).filter(Blog.user_id == user_id).distinct().all()

    @classmethod
    def get_recent_blog_by_user(cls, user_id):
        blog = Blog.query.filter_by(user_id == user_id).order_by('-id').first()
        return blog

    @classmethod
    def get_older_blog(cls, user_id, blog_id):
        blog = Blog.query.filter(Blog.user_id == user_id, Blog.id<blog_id).order_by('-id').first()

    @classmethod
    def get_newer_blog(cls, user_id, blog_id):
        blog = Blog.query.filter(Blog.user_id == user_id, Blog.id>blog_id).order_by('id').first()

class Blog(db.Model):
    blog_query = BlogQuery()
    __tablename__ = 'note'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column('user_id', db.Integer, nullable=False, key='user_id')
    time = db.Column('time', db.TIMESTAMP, nullable=False)
    update_time = db.Column('update_time', db.TIMESTAMP, nullable=False)
    content = db.Column('content', db.Text, nullable=False)

    def __init__(self, user_id, content, time):
        self.user_id = user_id
        self.time = time
        self.content = content
        self.update_time = time
    def __repr__(self):
        return "<Note id=%s, author_id=%s>" % (self.id, self.user_id)

    @classmethod
    def create(cls, user_id, content, time=None):
        if not time:
            time = datetime.datetime.now()
        blog = cls(user_id, content, time)
        db.session.add(blog)
        db.session.commit()

        return blog
    def update(self, content):
        self.content = content
        self.update_time = datetime.datetime.now()
        db.session.commit()

    @classmethod
    def gets_by_author(cls, user_id):
        return cls.query.filter_by(user_id = user_id).all()
