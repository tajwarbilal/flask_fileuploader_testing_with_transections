"""A simple flask web app"""
import os
from flask import Flask
from app.cli import create_database
from app.db import db
from app.db.models import User
import logging


def configure_logging():
    # register root logging
    logging.basicConfig(filename='bebu.log',level=logging.DEBUG)
    logging.getLogger('werkzeug').setLevel(logging.INFO)


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = 'This is an INSECURE secret!! DO NOT use this in production!!'

    db_dir = "app.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.abspath(db_dir)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from app.user.user_blueprint import user_blueprint
    app.register_blueprint(user_blueprint)

    from app.home.home_blueprints import home_blueprint
    app.register_blueprint(home_blueprint)

    # add command function to cli commands
    app.cli.add_command(create_database)
    app.app_context().push()
    db.create_all()
    configure_logging()
    app.logger.info('Application Has Been Created')

    return app
