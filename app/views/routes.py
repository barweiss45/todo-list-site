#! /usr/bin/env python3

from flask import abort, jsonify, render_template, request

from app.config import logger
from app.models import (ClientResponse, CompleteTask, CreateTask, TaskModel,
                        ValidationError)

from .. import db
from . import task_blueprint


@task_blueprint.route('/')
def index():
    return render_template('index.html')


@task_blueprint.route('/tasks/<int:id>', methods=["GET"])
def get_task(id: int) -> ClientResponse:
    """Get a single Task"""
    task = TaskModel.query.get_or_404(id)
    task_model = {
        "id": task.id,
        "task": task.task,
        "completed": task.completed
    }
    return jsonify({"success": True, "message": task_model}), 200


@task_blueprint.route('/tasks', methods=["GET"])
def get_tasks() -> ClientResponse:
    """Get all tasks"""
    tasks = TaskModel.query.all()
    task_list = []
    for task in tasks:
        task_model = {
            "id": task.id,
            "task": task.task,
            "completed": task.completed
        }
        task_list.append(task_model)
    return jsonify({"success": True, "message": task_list}), 200


@task_blueprint.route("/tasks/create", methods=["POST"])
def create():
    """Create a task"""
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
    """Complete a task"""
    try:
        task_data = CompleteTask(**request.json)  # Validate Pydantic model
    except ValidationError as e:
        return jsonify({"succcess": False, "message": str(e)}), 400
    task = TaskModel.query.get_or_404(id)
    task.completed = task_data.complete_data

    return jsonify({"success": True, "message": f"ID: {id} created."}), 200


@task_blueprint.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id) -> ClientResponse:
    """Delete a task"""
    task = TaskModel.query.get(id)
    if task is None:
        abort(404)  # Task not found, return 404 Not Found

    db.session.delete(task)
    db.session.commit()

    return jsonify({"success": True, "message": f"ID: {id} deleted. {task}"}), 200
