from fabric.api import sudo

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
    sudo('apt-get update', quiet=True)
    cuisine.package_ensure('build-essential')
    cuisine.package_ensure('git-core')


def _setup_python():
    """
    Install Python and Python related tools.
    """
    cuisine.package_ensure('python')
    cuisine.package_ensure('python-setuptools')
    sudo('easy_install pip', quiet=True)
    sudo('pip install -r /home/vagrant/src/requirements/development.txt',
         quiet=True)


def _extra_packages():
    """
    Install extra utils packages.
    """
    cuisine.package_ensure('tree')
    cuisine.package_ensure('figlet')
