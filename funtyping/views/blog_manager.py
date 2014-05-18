# -*- coding:utf-8 -*-

from funtyping import app
from funtyping.utils.util import get_user_id, format_textarea, get_local_weekday, get_local_date
from funtyping.models.blog import Blog, BlogQuery
from flask import redirect, session, render_template, url_for, request, jsonify
from random import randint
import cgi
import datetime

@app.route('/notes/<datenum>')
@app.route('/notes/')
def notes(datenum=None):
    user_id = get_user_id()
    blogs = Blog.blog_query.get_blog_by_author(user_id)
    if datenum is None:
        datenum = ''
    else:
        blogs = [blog for blog in blogs if str(blog.time) == datenum]
    if not blogs:
        return redirect(url_for('no_blogs'))
    for blog in blogs:
        blog.weekday = get_local_weekday(blog.time)
        blog.time = get_local_date(blog.time)
    date_list = [str(d) for d, in Blog.blog_query.get_datenum_by_user(user_id)]
    date_list = sorted(date_list,reverse=True)
    return render_template('note_list.html', notes = blogs, date_list = date_list, datenum = datenum)
@app.route('/get_notes_by_date')
def get_notes_by_date():
    user_id = get_user_id()
    datenum = int(request.args.get('datenum'))
    blogs = Blog.blog_query.get_blogs_by_datenum(user_id, datenum)
    json_blog_list = []
    for blog in blogs:
        blog.weekday = get_local_weekday(blog.time)
        blog.time = get_local_date(blog.time)
        json_note_list = json.dumps(new(blog),cls=MyEncoder)
    return json.dumps(json_note_list)

@app.route('/latest')
def latest():
    user_id = get_user_id
    blog = Blog.blog_query.get_recent_blog_by_user(user_id)
    if not blog:
        return redirect(url_for('no_notes'))
    blog.weekday = get_local_weekday(blog.time)
    blog.time = get_local_date(blog.time)
    return render_template('note.html', note=blog)

@app.route('/get_older_note', methods=['GET'])
def get_older_note():
    note_id = int(request.args.get('note_id'))
    user_id = get_user_id()
    blog = BlogQuery.get_older_blog(user_id, note_id)
    if not blog:
        blog = Blog.blog_query.get_blog_by_id(note_id)
    blog_id = blog.id
    blog_content = blog.content
    blog_weekday = get_local_weekday(blog.time)
    blog_time = get_local_date(blog.time)

    return jsonify(id = blog_id, weekday = blog_weekday, time = blog_time, content = blog_content)

@app.route('/get_newer_note', methods=['GET'])
def get_newer_note():
    note_id = int(request.args.get('note_id'))
    user_id = get_user_id()
    note = BlogQuery.get_newer_blog(user_id,note_id)
    if not note:
        note = BlogQuery.get_blog_by_id(note_id)
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(
                id = note_id,
                weekday = note_weekday,
                time = note_time,
                content = note_content
            )

# FIXME: 有可能获取到跟当前日记重复的日记，需过滤
@app.route('/get_random_note', methods=['GET'])
def get_random_note():
    note_id = int(request.args.get('note_id'))
    user_id = get_user_id()
    note_list = BlogQuery.get_blog_by_author(user_id)
    note = note_list[randint(0, len(note_list)-1)]
    note_id = note.id
    note_content = note.content
    note_weekday = get_local_weekday(note.time)
    note_time = get_local_date(note.time)
    return jsonify(
                id = note_id,
                weekday = note_weekday,
                time = note_time,
                content = note_content
            )

@app.route('/write',methods=['GET','POST'])
def write():
    if request.method == 'GET':
        return render_template('write.html')
    elif request.method == 'POST':
        note_date = request.form["note_date"]
        note_content = request.form["note_content"]
        note_content = cgi.escape(note_content)
        note_content = format_textarea(note_content)
        try:
            note_date = datetime.datetime.strptime(note_date, '%Y-%m-%d')
        except ValueError:
            note_date = datetime.datetime.now()

        user_id = get_user_id()
        Blog.create(user_id,  note_content, note_date)
        return redirect(url_for("notes"))

@app.route('/nonotes')
def no_notes():
    return render_template('no_notes.html')
