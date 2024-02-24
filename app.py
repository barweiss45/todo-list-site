import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from models import TaskModel, Task


load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']  = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
