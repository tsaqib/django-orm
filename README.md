# django-orm

A boilerplate to separate the ORM part of Django, so that it may be dropped in any project, ie. Flask app. It should 
play very nicely with any framework.  

## Steps

1. `pip install -r requirements.txt`
2. Change database connection info at `data_backend/settings.py`
3. `./manage.py makemigrations data_backend`
4. `./manage.py migrate`
5. `python main.py`