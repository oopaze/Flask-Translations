from flask import Flask
from flask_babel import Babel
from flask_migrate import Migrate

from .src.db import configure_db


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Development')

    configure_db(app)

    babel = Babel(app)
    Migrate(app, app.db)

    return app


app = create_app()
