# lanweb - dfekt LAN web project

# This webpage should be rewritten before the next dfekt LAN

## Setting up a dev enviroment

If you are using a *nix computer either virtualenv or Vagrant is good. If you are using Windows, Vagrant is the way to go.

### virtualenv

#### Install python-setuptools

`sudo apt-get install python-setuptools`

#### Install python-dev
`sudo apt-get install libpq-dev python-dev`

#### Install and initialize a virtual python environment

`sudo pip install virtualenv` || `sudo apt-get install python-virtualenv`

`sudo pip install virtualenvwrapper` || `sudo apt-get install virtualenvwrapper`

#### Add the following to your bashrc/zshrc file
`export WORKON_HOME=~/.environments`

`source /usr/local/bin/virtualenvwrapper.sh`

> You might need to specify the python binary, and virtualenv's path might also be different. On ArchLinux I had to add the following:

> `export WORKON_HOME=~/.environments`

> `export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2`

> `source /usr/bin/virtualenvwrapper.sh`

#### Source your shell's configuration file

`source ~/.zshrc` || `source ~/.bashrc`

#### Continune in shell ...

`mkvirtualenv lanweb`

#### Clone the lanweb repo at a location of your choosing
`git clone git@github.com:kradalby/lanweb.git`

`cd lanweb`

`pip install -r requirements.txt`

### Vagrant

* Host machine:
 * Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
 * Install [Vagrant](http://vagrantup.com/)
 * `git clone git@github.com:kradalby/lanweb.git`
 * `cd lanweb`
 * `vagrant up`
 * `vagrant ssh`

* Guest machine:
 * `cd /vagrant`
 * `sudo pip install -r requirements.txt`
 * `python manage.py syncdb --migrate`
 * `python manage.py runserver 0.0.0.0:8000`
