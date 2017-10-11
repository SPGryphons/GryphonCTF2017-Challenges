#!/bin/bash

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install apache2
sudo apt-get -y install php7.0 php7.0-sqlite3
sudo systemctl restart apache2
sudo cp -r webapp/* /var/www/html