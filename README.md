# grocery-app
Grocery Application

Setup flask database:
```shell
export FLASK_APP=src/wsgi.py # depends on the location of this file
flask db init
flask db migrate -m "message here"
flask db upgrade
```