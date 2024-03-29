from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime
import os



db = SQLAlchemy()

        
def create_app(script_info=None):
    app = Flask(__name__)

    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object('project.config.DevelopmentConfig')

    db.init_app(app)

    from project.api.users import users_blueprint
    app.register_blueprint(users_blueprint)

    app.shell_context_processor({"app":app, "db":db})
    return app