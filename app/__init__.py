import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .routes import blueprint


# create Flask and SQLAlchemy instances
app = Flask(__name__)
db = SQLAlchemy()

# configuration
db_name = 'database.db'
app.config.from_mapping(
    SECRET_KEY = 'h4sski',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + db_name,
    SQLALCHEMY_TRACK_MODIFICATIONS = True,
)

app.register_blueprint(blueprint=blueprint)


if __name__ == '__main__':
    # debuging
    app.run(debug=True)

    # production
    # app.run()
