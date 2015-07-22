# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  unless Vagrant::Util::Platform.windows? and not(Vagrant.has_plugin?("vagrant-winnfsd"))
    config.vm.synced_folder ".", "/vagrant", type: "nfs"
  end

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provider "virtualbox" do |vb|
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y build-essential libssl-dev libffi-dev python-dev libxml2-dev libxslt1-dev
    sudo apt-get install -y python-pip
    sudo pip install scrapy
    scrapy version
  SHELL
end
