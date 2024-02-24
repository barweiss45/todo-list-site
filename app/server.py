import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

from models import Task, TaskModel

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)
tz = timezone.utc


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/tasks', methods=['POST'])
def create_task():
    try:
        task_data = Task(**request.json)  # Validate incoming JSON data with Pydantic
        new_task = TaskModel(task=task_data.task,
                             completed=task_data.completed,
                             create_date=datetime.astimezone(tz).now())  # Create an SQLAlchemy model instance
        db.session.add(new_task)
        db.session.commit()
        return jsonify({"success": True, "task": task_data.dict()}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
