#!/bin/bash -xe
#/etc/init.d/mysql start
#/etc/init.d/redis-server start

mysql -e "CREATE DATABASE lsofadmin"
mysql -e "GRANT ALL ON lsofadmin.* to 'lsofadmin'@'localhost' identified by 'lsofadmin'"
mysql -e "FLUSH PRIVILEGES"

pip3 install -r requirements.txt

## Make migrations
python3 manage.py makemigrations
python3 manage.py makemigrations dns
python3 manage.py migrate

## Run
python3 manage.py tests lsofadmin
cat <<EOF > create_user.py
# this must happen before we try to import objects
import django
django.setup()

from django.contrib.auth.models import User
user = User.objects.create_user('loadtest', password='loadtest')
user.is_superuser = False
user.is_staff = False
user.save()

from lsofadmin.dns.models import Domain
domain = Domain.objects.create_domain("lsof.top")
EOF

# https://stackoverflow.com/questions/26082128/improperlyconfigured-you-must-either-define-the-environment-variable-django-set
DJANGO_SETTINGS_MODULE=lsofadmin.settings python3 create_user.py
if [ ! $? -eq 0 ]; then
    exit 1
fi

# Create the API key we use in the loadtest requests
API_KEY="abc123"
CURDATE=$(date "+%Y-%m-%d %T.%N")
SQL_QUERY="INSERT INTO authtoken_token (\`key\`, created, user_id) VALUES ('${API_KEY}', '${CURDATE}', 1)"
mysql -e "${SQL_QUERY}" lsofadmin
