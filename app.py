from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        todos.append(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    if 0 <= id < len(todos):
        todos.pop(id)
    return redirect(url_for("index"))


