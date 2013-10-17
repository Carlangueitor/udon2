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
    sudo('apt-get update')
    cuisine.package_ensure('build-essential')
    cuisine.package_ensure('git-core')


def _setup_python():
    """
    Install Python and Python related tools.
    """
    cuisine.package_ensure('python')


def _extra_packages():
    """
    Install extra utils packages.
    """
    cuisine.package_ensure('tree')
    cuisine.package_ensure('figlet')
