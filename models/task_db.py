#! /usr/bin/env/ python3

from app import db


class TaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    create_date = db.Column(db.String, varchar=True)


class CreateToDo(BaseToDo):
    pass


class Modify(BaseToDo):
    pass
