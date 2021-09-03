# README #

API for the PetHub App.

### Prerequisite ###
* Django
* Django Rest Framework
* Postgres


### How to setup on your local device ###

1. after cloning this repo, cd to the project folder.

2. setup your environment on (/pet-hub/pethub/):
	- python3 -m venv env 
	- source env/bin/env

3. Install other dependencies:
	- pip install -r requirments.txt

4. Setup database in Postgres:
	- sh scripts/setup_db.sh

5. Setup migrations:
	- sh scripts/setup_migration.sh

6. Setup initial data:
	- sh scripts/setup_data.sh

7. Run server:
	- python manage.py runserver 

8. Access via localhost:8000/v1/

### API Docs can be found at ###

* http://localhost:8000/swagger/