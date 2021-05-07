import mysql.connector
import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g:
        g.db=mysql.connector.connect(
            host='localhost',
            user= 'root',
            password= '',
            database= 'peganos'

        )
        g.c = g.db.cursor(dictionary = True)
    return g.db, g.c

def close_db(e = None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)