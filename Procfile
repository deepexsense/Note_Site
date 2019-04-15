release: python manage.py makemigratons
release: python manage.py migrate
web: gunicorn NoteSite.wsgi --log-file -
