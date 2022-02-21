release: python manage.py makemigrations --noinput
release: python manage.py migrate --noinput

web: gunicorn tyson_api.wsgi