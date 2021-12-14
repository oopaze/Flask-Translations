from flask import Flask
from flask_migrate import Migrate

from .src.db import configure_db
from .src.babel import configure_babel

from .task.routes import task_bp as TaskBluePrint


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Development')

    configure_db(app)
    configure_babel(app)

    Migrate(app, app.db)

    app.register_blueprint(TaskBluePrint)

    return app


app = create_app()
