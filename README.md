# djangocrashcourse

Very simple Django blog app for Traversy crash course

Old: https://www.youtube.com/watch?v=D6esTdOLXh4

New: https://www.youtube.com/watch?v=e1IyzVyrLSU + https://github.com/bradtraversy/pollster_django_crash

$ virtualenv py1

$ source py1/bin/activate

$ pip install django

Mac: problems with MySQL
$ brew install mysql-client

#### mysql-client is not on the `PATH` by default

export PATH="/usr/local/opt/mysql-client/bin:$PATH"

or:
❯ echo 'export PATH="/usr/local/opt/ruby/bin:$PATH"' >> ~/.zshrc
❯ export LDFLAGS="-L/usr/local/opt/mysql-client/lib"
❯ export CPPFLAGS="-I/usr/local/opt/ruby/include"
❯ export PKG_CONFIG_PATH="/usr/local/opt/mysql-client/lib/pkgconfig"

#### openssl is not on the link path by default

export LIBRARY_PATH="$LIBRARY_PATH:/usr/local/opt/openssl/lib/"
Then $ pip wheel mysqlclient / $ pip install mysqlclient

First: make it fill the DB:

$ python manage.py migrate

$ python manage.py createsuperuser --username=admin --email=email@email.com

prompt for passwod: abc123!!

$ python manage.py runserver

fun: $ python manage.py inspectdb

- not needed: django-admin startproject djangoproject
- not needed: $ pip install mysql-connector-python / $ pip install pymysql
