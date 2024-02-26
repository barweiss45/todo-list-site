#! /usr/bin/env python3

from flask import jsonify, redirect, render_template, request, url_for
from app.models import TaskModel, CreateTask, CompleteTask, ValidationError, ClientResponse

from .. import db
from . import task_blueprint
from instance.config import logger


@task_blueprint.route('/')
def index():
    return render_template('index.html')


@task_blueprint.route("/tasks/create", methods=["POST"])
def create():
    try:
        task_data = CreateTask(**request.json)  # Validate incoming JSON data with Pydantic
        new_task = TaskModel(task=task_data.task,
                             completed=task_data.completed)  # Create an SQLAlchemy model instance
        db.session.add(new_task)
        db.session.commit()
        logger.info("/create_task - R_IP: %s",  request.remote_addr)
        return jsonify({"success": True, "message": task_data.model_dump()}), 201
    except (ValueError, ValidationError) as e:
        logger.error(e)
        return jsonify({"success": False, "message": str(e)}), 400


@task_blueprint.route("/tasks/<int:id>/complete", methods=["PUT"])
def complete(id: int) -> ClientResponse:
    try:
        task_data = CompleteTask(**request.json)  # Validate Pydantic model
    except ValidationError as e:
        return jsonify({"succcess": False, "message": str(e)}), 400
    task = TaskModel.query.get_or_404(id)
    task.completed = task_data.complete_data

    return jsonify({"success": True, "message": "Created"}), 200


# Add more routes as needed
