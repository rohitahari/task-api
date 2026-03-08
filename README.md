# Task Management API

A RESTful backend API for managing tasks built with FastAPI. The API supports creating, retrieving, updating, and deleting tasks with persistent storage using SQLite.

## Features

- Create tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Persistent storage with SQLite
- Interactive API documentation

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- Uvicorn

## Project Structure

task-api/
│
├── main.py
├── requirements.txt
├── README.md

## Installation

Install dependencies:

pip install -r requirements.txt

## Run the API Server

uvicorn main:app --reload

## API Documentation

After starting the server open:

http://127.0.0.1:8000/docs

FastAPI automatically generates interactive documentation where you can test the endpoints.

## API Endpoints

GET /tasks  
POST /tasks  
PUT /tasks/{task_id}  
DELETE /tasks/{task_id}

## Example Response

{
  "id": 1,
  "title": "Study FastAPI"
}

## License

MIT
