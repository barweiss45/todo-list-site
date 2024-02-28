#! /usr/bin/env/ python3

from .. import db


class TaskModel(db.Model):
    """
    TaskModel - Database Schema

    Example:
    {
        "id": 1,
        "task": "Complete this todo application.",
        "completed": False
    }
    """
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False)
