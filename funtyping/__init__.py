#-*- coding:utf-8 -*-

from flask import Flask 
app = Flask("funtyping")
app.config.from_pyfile('app_config.cfg')

