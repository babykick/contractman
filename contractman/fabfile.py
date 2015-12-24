from fabric.api import run, env
from fabric.context_managers import cd

env.use_ssh_config = True

def deploy():
    with cd('/home/stephen/workspace/python/contractman/'):
        run('ls')
        run('git fetch')
        run('git reset --hard origin/master')
        run('cd contractman && source migrate.bat')