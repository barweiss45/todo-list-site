"""
Factory Function for Flask Application
"""

import os

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()


def create_app():
    """Factory Function for Flask Application"""
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

    db.init_app(app)

    with app.app_context():
        from app.models import \
            TaskModel  # Import models here to register them with SQLAlchemy

        # Import Blueprints and register them
        from .views import task_blueprint
        app.register_blueprint(task_blueprint)

    return app
