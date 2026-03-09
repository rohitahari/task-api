Task Manager Web Application

A simple full-stack task management web application that allows users to create, update, complete, and delete tasks.

Built using FastAPI for the backend, SQLite for the database, and a lightweight JavaScript frontend.

---

Features

- Add new tasks
- Edit existing tasks
- Delete tasks
- Mark tasks as completed
- Persistent storage using SQLite
- Interactive UI with real-time updates

---

Tech Stack

Backend:

- FastAPI
- SQLAlchemy
- SQLite

Frontend:

- HTML
- CSS
- JavaScript (Fetch API)

---

Application Architecture

Browser UI
↓
JavaScript Requests
↓
FastAPI Backend API
↓
SQLite Database

---

Installation

Clone the repository:

git clone https://github.com/rohitahari/task-api.git

Navigate into the project directory:

cd task-api

Install dependencies:

pip install fastapi uvicorn sqlalchemy jinja2

Run the application:

uvicorn main:app --reload

---

Usage

Open the browser and navigate to:

http://127.0.0.1:8000

You can now:

- Add tasks
- Edit tasks
- Delete tasks
- Mark tasks as completed

---

API Endpoints

GET /tasks
Retrieve all tasks

POST /tasks
Create a new task

PUT /tasks/{task_id}
Update a task

PUT /tasks/{task_id}/toggle
Toggle task completion

DELETE /tasks/{task_id}
Delete a task

---

Project Structure

task-api/
│
├── main.py
├── templates/
│   └── index.html
├── tasks.db
└── README.md

---

Learning Objectives

This project demonstrates:

- Building REST APIs with FastAPI
- Database integration using SQLAlchemy
- CRUD operations
- Full-stack application architecture
- Connecting a JavaScript frontend with a Python backend

---

Author

Rohit Ahari
