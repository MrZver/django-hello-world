import os, sys
sys.path.append('D:/Workspace/github/django-hello-world')
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_study.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()