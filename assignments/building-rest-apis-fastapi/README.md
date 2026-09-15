# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice creating endpoints, validating request data, and returning JSON responses for a simple resource such as tasks or books.

## 📝 Tasks

### 🛠️ Set Up a FastAPI App

#### Description
Create a basic FastAPI application and run it locally so you can test your API with the browser or an HTTP client.

#### Requisitos
O programa concluído deve:

- Install `fastapi` and `uvicorn` in the environment.
- Create an app instance using `FastAPI()`.
- Add a root endpoint such as `/` that returns a welcome message in JSON.
- Run the application with `uvicorn main:app --reload`.
- Confirm that the server starts successfully without errors.

### 🛠️ Create a Task Resource

#### Description
Implement a simple in-memory task API that stores task data and exposes it through REST endpoints.

#### Requisitos
O programa concluído deve:

- Define a `Task` model with fields such as `id`, `title`, `description`, and `completed`.
- Create a list to store tasks in memory.
- Add a `GET /tasks` endpoint that returns all tasks.
- Add a `POST /tasks` endpoint that accepts a new task and returns the created task.
- Return HTTP status `201 Created` for successful task creation.
- Validate required fields such as `title` before saving the task.

### 🛠️ Add Detail and Update Endpoints

#### Description
Extend the API with endpoints for retrieving, updating, and deleting a single task.

#### Requisitos
O programa concluído deve:

- Add a `GET /tasks/{task_id}` endpoint that returns one task by ID.
- Add a `PUT /tasks/{task_id}` endpoint that updates an existing task.
- Add a `DELETE /tasks/{task_id}` endpoint that removes a task.
- Return a `404 Not Found` response when a task does not exist.
- Use meaningful response messages and JSON payloads for each operation.

