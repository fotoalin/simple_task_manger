from datetime import datetime

from flask import (
    Flask,
    redirect,
    render_template,
    render_template_string,
    request,
    url_for,
)

from models import Database, Task
from tasks import dummy_tasks

app = Flask(__name__)

from flask import request

from tasks import dummy_tasks

db = Database()

for task in dummy_tasks:
    db.add(Task(content=task))

print(db.all())


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        context = {"tasks": db.all()}
        return render_template("index.html", context=context)

    return redirect(url_for("index"))


@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        task_content = request.form["task"]
        new_task = Task(content=task_content)
        db.add(new_task)
    return redirect(url_for("index", context=db.all()))


@app.route("/delete/<string:id>", methods=["POST"])
def delete(id):
    task = db.get(id)
    if task:
        db.delete(task)
        print("Task deleted")
    else:
        print("Task not found")
    return redirect(url_for("index"))


@app.route("/complete/<string:id>", methods=["POST"])
def complete(id):
    task = db.get(id)
    if task:
        task.completed = True
        print("Task completed")
    else:
        print("Task not found")
    return redirect(url_for("index"))


@app.route("/edit/<string:id>", methods=["POST"])
def edit(id):
    task = db.get(id)
    if task:
        return render_template("task-edit.html", task=task)
    else:
        print("Task not found")
    return redirect(url_for("index"))


@app.route("/update/<string:id>", methods=["POST"])
def update(id):
    task = db.get(id)
    if task:
        new_content = request.form["new_content"]
        db.update(task, new_content)
        print("Task updated")
    else:
        print("Task not found")
    return new_content


@app.route("/search", methods=["POST"])
def search():
    term = request.form.get("term", None)
    if term == "" or term is None or term.isspace() or term == "*":
        tasks = db.all()
    else:
        tasks = db.search(term)
    context = {"tasks": tasks}

    return render_template("tasks.html", context=context)


if __name__ == "__main__":
    app.run(debug=True)
