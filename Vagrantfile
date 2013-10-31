# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  
    config.vm.box = "precise32"
    config.vm.synced_folder "src/", "/home/vagrant/src/", create: true, owner: 'vagrant', group: 'vagrant', mount_options: ['dmode=777,fmode=666']
    config.vm.network "forwarded_port", guest: 8000, host: 8000

    config.vm.provision :fabric do |fabric|
        fabric.fabfile_path = "./provision.py"
        fabric.tasks = ["provide"]
    end
end
