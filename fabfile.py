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


@task
def bootstrap():
    """
    Bootstrap Environment.
    """
    run("createdb udon")
    _syncdb()


# manage.py tasks

@task
def _syncdb():
    """
    Run syncdb command.
    """
    require('site_dir')
    with cd(env.site_dir):
        run("python manage.py syncdb")


@task
def migrate(app=None):
    """
    Run migrations for selected app or all apps.
    """
    require('site_dir')
    with cd(env.site_dir):
        run("python manage.py migrate {0}".format(app or ''))


@task
def syncdb():
    """
    Run syncdb and migrations for all apps.
    """
    _syncdb()
    migrate()


@task
def runserver():
    """
    Run the Django development server.
    """
    require('site_dir')
    with cd(env.site_dir):
        run("python manage.py runserver_plus 0.0.0.0:8000 --traceback")


@task
def migration(app, intitial=False):
    """
    Create schemamigration for selected app.
    """
    require('site_dir')
    with cd(env.site_dir):
        if intitial:
            run("python manage.py schemamigration {0} --initial".format(app))
        else:
            run("python manage.py schemamigration {0} --auto".format(app))
