#export DJANGO_SETTINGS_MODULE=config.settings
nohup gunicorn -k gevent config.wsgi:application -c ./gunicorn.conf.py&