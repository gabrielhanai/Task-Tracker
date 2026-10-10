from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []
doings = []
dones = []

@app.route("/")
def index():
    return render_template("index.html", todos=todos, doings=doings, dones=dones)

@app.route("/addtodo", methods=["POST"])   
def addtodo(): 
    todo = request.form.get("todo")
    if todo:
        todos.append(todo)
    return redirect(url_for("index"))

@app.route("/adddoing", methods=["POST"])
def adddoing():
    doing = request.form.get("doing")
    if doing:
        doings.append(doing)
    return redirect(url_for("index"))

@app.route("/adddone", methods=["POST"])
def adddone():
    done = request.form.get("done")
    if done:
        dones.append(done)
    return redirect(url_for("index"))

@app.route("/limpar", methods=["POST"])
def limpar():
    todos.clear()
    doings.clear()
    dones.clear()
    return redirect(url_for("index"))