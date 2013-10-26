from fabric.api import sudo
from fabric.colors import blue

import cuisine


cuisine.select_package("apt")


def provide():
    _setup_ubuntu()
    _setup_python()
    _extra_packages()


def _setup_ubuntu():
    """
    Update packages and install basic packages.
    """
    print blue("Updating System")
    sudo('apt-get update', quiet=True)
    print blue("Installing Basic Packages")
    cuisine.package_ensure('build-essential')
    cuisine.package_ensure('git-core')


def _setup_python():
    """
    Install Python and Python related tools.
    """
    print blue("Setup Python")
    cuisine.package_ensure('python')
    cuisine.package_ensure('python-setuptools')
    cuisine.package_ensure('python2.7-dev')
    cuisine.package_ensure('libjpeg-dev')
    cuisine.package_ensure('libjpeg62')
    cuisine.package_ensure('libjpeg62-dev')
    cuisine.package_ensure('zlib1g-dev')
    cuisine.package_ensure('libfreetype6')
    cuisine.package_ensure('libfreetype6-dev')
    sudo('easy_install pip', quiet=True)
    print blue("Installing python requirements.")
    sudo('pip install -r /home/vagrant/src/requirements/development.txt',
         quiet=True)


def _extra_packages():
    """
    Install extra utils packages.
    """
    print blue("Installing extra packages.")
    cuisine.package_ensure('tree')
    cuisine.package_ensure('figlet')
