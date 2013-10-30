from fabric.api import task, require, run, local, env, cd


# Environments
@task
def vagrant():
    """
    Local development Vagrant machine.
    """
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    key = local("vagrant ssh-config | grep IdentityFile", capture=True)
    env.key_filename = key.split()[1]
    env.site_dir = "~/src"


# manage.py tasks
@task
def runserver():
    """
    Run the Django development server.
    """
    require('site_dir')
    with cd(env.site_dir):
        run("python manage.py runserver_plus 0.0.0.0:8080 --traceback")
