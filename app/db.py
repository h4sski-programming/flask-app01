import sqlite3
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()


def with_db_open(inner_function, *args, **kwargs):
    database = get_db()
    result = inner_function(db=database, *args, **kwargs)
    close_db()
    return result