release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: sh scripts/setup_data.sh


web: gunicorn pethub.wsgi