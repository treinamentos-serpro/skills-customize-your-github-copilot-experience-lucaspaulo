from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

tasks = [
    {"title": "Learn Flask routes", "completed": True},
    {"title": "Build a form", "completed": False},
]


@app.get("/")
def home():
    return render_template("index.html", tasks=tasks)


@app.post("/tasks")
def add_task():
    title = request.form.get("title", "").strip()

    # TODO: Validate the title and show an error on the home page when it is empty.
    if not title:
        return render_template("index.html", tasks=tasks, error="")

    tasks.append({"title": title, "completed": False})
    return redirect(url_for("home"))
