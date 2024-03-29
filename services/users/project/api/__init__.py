import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
toobar = DebugToolbarExtension()

def create_app(script_info=None):

    app = Flask(__name__)

    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)


    db.init_app(app)
    toolbar.init_app(app)

    from project.api.users import users_blueprint
    app.register(users_blueprint)
    app.shell_context_processors({'app':app, "db":db})

    return db
    