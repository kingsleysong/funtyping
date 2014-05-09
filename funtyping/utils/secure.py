# -*- coding:utf-8 -*-

import hashlib
import random

def encrypt(password):
    salt = ''.join(random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*()',10))
    hash = hashlib.md5(salt+password).hexdigest()
    return salt,hash

def check_user(password, salt, real_password):
    return hashlib.md5(salt+password).hexdigest() == real_password
