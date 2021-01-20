# -*- mode: ruby -*-
# vi: set ft=ruby :

supported_os = {
  :ubuntu => { :version => "bionic64", :network => { :host => 8080 } }
}

unless Vagrant.has_plugin?("vagrant-disksize")
  raise 'vagrant-disksize is not installed!'
end

Vagrant.configure("2") do |config|
  supported_os.each do |os, os_parameters|
    config.vm.define os do |vm_config|
      vm_config.vm.box = "#{os}/#{os_parameters[:version]}"
      vm_config.disksize.size = "1GB"

      # Create a forwarded port mapping which allows access to a specific port
      # within the machine from a port on the host machine and only allow access
      # via 127.0.0.1 to disable public access
      vm_config.vm.network "forwarded_port", guest: 80, host: os_parameters[:network][:host], host_ip: "127.0.0.1"

      # Create a private network, which allows host-only access to the machine
      # using a specific IP.
      # vm_config.vm.network "private_network", ip: "192.168.33.10"

      # Share an additional folder to the guest VM. The first argument is
      # the path on the host to the actual folder. The second argument is
      # the path on the guest to mount the folder. And the optional third
      # argument is a set of non-required options.
      # vm_config.vm.synced_folder "../data", "/vagrant_data"

      # Provider-specific configuration so you can fine-tune various
      # backing providers for Vagrant. These expose provider-specific options.
      vm_config.vm.provider "virtualbox" do |vb|
        # Customize the amount of memory on the VM:
        vb.memory = "1024"
        # Disable logs generation on host
        vb.customize [ "modifyvm", :id, "--uartmode1", "disconnected" ]
      end

      # Enable provisioning with a shell script. Additional provisioners such as
      # Ansible, Chef, Docker, Puppet and Salt are also available. Please see the
      # documentation for more information about their specific syntax and use.
      vm_config.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/vagrant_host.pub"
      vm_config.vm.provision "shell", inline: <<-SHELL
        cat /home/vagrant/.ssh/vagrant_host.pub >> /home/vagrant/.ssh/authorized_keys
      SHELL
    end
  end
end
