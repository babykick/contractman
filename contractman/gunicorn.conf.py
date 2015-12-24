import multiprocessing

bind = "0.0.0.0:9206"
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = './gunicorn.error.log'
accesslog = './gunicorn.access.log'
#loglevel = 'debug'
proc_name = 'gunicorn_onemile_project'
