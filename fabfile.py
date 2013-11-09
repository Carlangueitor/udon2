from fabric.api import task, require, run, local, env, cd, settings
from fabric.colors import red, green


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


@task
def shell():
    """
    Run Django shell.
    """
    require('site_dir')
    with cd(env.site_dir):
        run("python manage.py shell_plus")


@task
def test(app=None):
    """
    Run django tests.
    """
    require('site_dir')
    with cd(env.site_dir):
        with settings(warn_only=True):
            result = run("coverage run --source='.' manage.py test "
                         "--settings=udon.settings.testing {0}".format(app or ''),
                         combine_stderr=True)
            if result.return_code == 0:
                print green(" ____   _    ____ ____  _____ ____\n"
                            "|  _ \ / \  / ___/ ___|| ____|  _ \\\n"
                            "| |_) / _ \ \___ \___ \|  _| | | | |\n"
                            "|  __/ ___ \ ___) |__) | |___| |_| |\n"
                            "|_| /_/   \_\____/____/|_____|____/ ")
            else:
                print red(" _____ _    ___ _     _____ ____\n"
                          "|  ___/ \  |_ _| |   | ____|  _ \\\n"
                          "| |_ / _ \  | || |   |  _| | | | |\n"
                          "|  _/ ___ \ | || |___| |___| |_| |\n"
                          "|_|/_/   \_\___|_____|_____|____/ ")


@task
def report():
    """
    Run coverage report.
    """
    require('site_dir')
    with cd(env.site_dir):
        run('coverage report')
