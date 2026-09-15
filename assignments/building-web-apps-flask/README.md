# 📘 Assignment: Building Web Apps with Flask

## 🎯 Objective

Build a small web application with Flask to practice routes, HTML templates, form handling, and basic input validation. You will create a simple To-Do Board where users can view tasks and add new ones.

## 📝 Tasks

### 🛠️ Set Up the Flask App

#### Description

Create and run a Flask application that serves a home page for the To-Do Board.

#### Requisitos
O programa concluído deve:

- Install `flask` in the environment.
- Create a Flask application instance in `app.py`.
- Add a `GET /` route that renders an HTML template.
- Start the application locally with `flask --app app run --debug`.
- Display a page title and a short welcome message in the browser.

### 🛠️ Display To-Do Items

#### Description

Add an in-memory collection of tasks and show the current tasks on the home page using a Jinja template.

#### Requisitos
O programa concluído deve:

- Store at least three tasks in a Python list of dictionaries.
- Display every task in an HTML list.
- Show each task's title and whether it is completed.
- Use a Jinja `for` loop in the template instead of building HTML in Python.
- Show a clear message when there are no tasks to display.

### 🛠️ Add and Validate Tasks

#### Description

Create a form that allows a user to add a new task from the browser. Validate the submitted title before adding it to the collection.

#### Requisitos
O programa concluído deve:

- Add a form on the home page with a text input named `title` and a submit button.
- Handle form submissions with `POST /tasks`.
- Strip leading and trailing whitespace from the submitted title.
- Reject an empty title and show an error message without adding a task.
- Add valid tasks to the in-memory collection and redirect the user back to `/`.
- Preserve previously added tasks while the server is running.

Example valid submission:

```text
Title: Review loops
Result: The task appears in the To-Do Board
```

Example invalid submission:

```text
Title: [only spaces]
Result: Please enter a task title
```
