#Gift Express @ NTUMCSA 2015

#Introduction

The initial usage of Gift Express is the Christmas Party 2015, hosted by NTUMCSA.  
The main purpose is to help guests to match their partners to exchange their gifts with others.  
We suppose that gift exchange between male and femals has the higher priority.  
* NTUMCSA : Mainland China Student Association @ National Taiwan University  

##Environment

Debug Environment: Ubuntu 15.10, python 2.7.10, Django 1.8.7, SQLite  
Running Environment: Ubuntu 14.04LTS, python 2.7.10, Django 1.8.7, SQLite @ DigitOcean, Singapore  

##Quick Start

1. Download the file from git.
2. Migrate the database of Django
```
python manage.py makemigrations
python manage.py migrate
```
3. Create the superuser account of Django (if necessary)
```
python manage.py createsuperuser
```
4. Run server and enjoy it
```
python manage.py runserver 0.0.0.0:port
```
5. Access to the admin on Internet Brower (if necessary)
```
http://ip_address:port/admin
```