#coding=utf8

#SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

AUTHOR = 'YepMoon'

# this is useful for submitting markdow files
# when publish new articles
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

TOKEN = 'ucantguess'

CSRF_ENBLED = True
SECRET_KEY = 'ucantguess'

# OPENID_PROVIDERS = [
# {'name': 'baidu','url': 'http://www.baidu.com'}
# ]
