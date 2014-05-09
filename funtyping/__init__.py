#-*- coding:utf-8 -*-

from flask import Flask 
from funtyping.utils.util import get_user_id

app = Flask("funtyping")
app.config.from_object('funtyping.app_config')

app.jinja_env.globals.update(static='/static')
app.jinja_env.globals.update(get_user_id=get_user_id)

import views
