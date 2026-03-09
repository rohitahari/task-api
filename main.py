from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from sqlalchemy import Boolean


app = FastAPI()
templates = Jinja2Templates(directory="templates")

DATABASE_URL = "sqlite:///./tasks2.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)




@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    return tasks

@app.post("/tasks")
def create_task(title: str):
    db = SessionLocal()

    new_task = Task(title=title)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted"}



@app.put("/tasks/{task_id}")
def update_task(task_id: int, title: str):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    task.title = title

    db.commit()
    db.refresh(task)

    return task


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request":
                                                      request})


@app.put("/tasks/{task_id}/toggle")
def toggle_task(task_id: int):
    db = SessionLocal()

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    task.completed = not task.completed

    db.commit()
    db.refresh(task)

    return task
