from .base import *
# import django_heroku # used only in production of heroku apps


DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.01', 'domain.ext']
SUPER_SECRET_KEY = 'SECRET_KEY'
# django_heroku.settings(locals())