bind = 'unix:///tmp/gunicorn_mp_django.sock'
worders = 4
reload = False
chdir = '/home/pencil/code/mysite/Django_project_meetpencil'
raw_env = ['DJANGO_SETTINGS_MODULE=meetpencil.settings']

