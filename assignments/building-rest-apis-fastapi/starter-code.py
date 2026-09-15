from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks = [
    Task(id=1, title="Write project plan", description="Outline the API features", completed=False),
    Task(id=2, title="Review requirements", description="Check the acceptance criteria", completed=True),
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task API!"}


@app.get("/tasks")
def get_tasks():
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    new_task = Task(id=len(tasks) + 1, **task.model_dump())
    tasks.append(new_task)
    return new_task


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    for index, current_task in enumerate(tasks):
        if current_task.id == task_id:
            updated_task = Task(id=task_id, **task.model_dump())
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return {"message": f"Task {task_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
