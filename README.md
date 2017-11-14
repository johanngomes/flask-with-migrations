# flask-with-migrations

1. Install Flask, SQLAlchemy and Alembic, using:

```
pip install flask
pip install sqlalchemy
pip install alembic
```

2. Change the PostgreSQL connection URI to match yours, in apps/app.py, apps/app_without_flask_plugin.py and alembic.ini.

3. Run the project using:

```
py apps/app_without_flask_plugin.py
```

If you want to use the app with flask plugin to connect Flask and SQLAlchemy, you should instead use:

```
pip install flask-sqlalchemy
py apps/app.py
```

4. To test the migrations, after running the application for the first time, you will need to change Example model. Try to add a new column, for example.

Do the following commands, to do a migration:

```
alembic init alembic
alembic revision --autogenerate -m 'Added <name-of-column-you-added> into Example'
alembic upgrade head
```