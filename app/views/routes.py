#! /usr/bin/env python3

from flask import jsonify, redirect, render_template, request, url_for
from app.models import TaskModel, CreateTask

from .. import db
from . import task_blueprint


@task_blueprint.route('/')
def index():
    return render_template('index.html')


@task_blueprint.route("/create_task", methods=["POST"])
def create_task():
    try:
        task_data = CreateTask(**request.json)  # Validate incoming JSON data with Pydantic
        new_task = TaskModel(task=task_data.task, completed=task_data.completed)  # Create an SQLAlchemy model instance
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"success": True, "task": task_data.model_dump()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Add more routes as needed
