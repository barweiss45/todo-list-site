# app/views/__init__.py

from flask import Blueprint

task_blueprint = Blueprint('task', __name__)

from . import routes  # Import routes at the end to avoid circular dependencies
