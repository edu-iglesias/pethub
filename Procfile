release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
#release: python scripts/fixtures/initial_data.py --no-input

web: gunicorn pethub.wsgi