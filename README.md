The goal of this assignment was to learn about this type of database and different ways of working with it. This was accomplished by building a simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. We didn't actually upload anything, just made model instances and used them to represent real data.

Steps:

Clone this repo to your local machine.

Poetry install.

Poetry shell.

Python manage.py createsuperuser.

Python manage.py makemigrations.

Python manage.py migrate.

Python manage.py runserver.