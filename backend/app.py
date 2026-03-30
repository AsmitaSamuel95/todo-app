from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    new_task = Task(title=data["title"])

    db.session.add(new_task)
    db.session.commit()

    return {"message": "Task created"}, 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()

    result = []
    for task in tasks:
        result.append({
            "id": task.id,
            "title": task.title,
            "completed": task.completed
        })

    return result

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return {"message": "Task deleted"}

@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)

    data = request.get_json()
    task.completed = data["completed"]

    db.session.commit()

    return {"message": "Task updated"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)