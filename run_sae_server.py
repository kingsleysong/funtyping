#-*- coding:utf-8 -*-
from funtyping import app
from flaskext.actions import Manager

if __name__ == '__main__':
    manager = Manager(app,default_help_actions=False)
    manager.run()
