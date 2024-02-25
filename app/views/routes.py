#! /usr/bin/env python3

from . import task_blueprint
from flask import render_template, request, redirect, url_for, jsonify
from .. import db


@task_blueprint.route('/')
def index():
    return render_template('index.html')


@task_blueprint.route("/create_task", method=["POST"])
def create_task():
    try:
        task_data = Task(**request.json)  # Validate incoming JSON data with Pydantic
        new_task = TaskModel(task=task_data.task, completed=task_data.completed)  # Create an SQLAlchemy model instance
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"success": True, "task": task_data.dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
 

# Add more routes as needed
