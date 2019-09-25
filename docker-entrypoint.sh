#!/bin/bash -xe
/etc/init.d/mysql start
/etc/init.d/redis-server start

mysql -e "CREATE DATABASE lsofadmin"
mysql -e "GRANT ALL ON lsofadmin.* to 'lsofadmin'@'localhost' identified by 'lsofadmin'"
mysql -e "FLUSH PRIVILEGES"

pip3 install -r requirements.txt

## Make migrations
python3 manage.py makemigrations
python3 manage.py makemigrations dns
python3 manage.py migrate
