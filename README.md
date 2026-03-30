# Todo App (Flask + React + SQLite)

A simple full-stack Todo application built with Flask (backend), React (frontend), and SQLite (database).

## Project Structure

<pre> ```text todo-app/ ├── backend/ ├── frontend/ ``` </pre>

## Backend Setup

1. Navigate to backend folder:
   cd backend

2. Create virtual environment:
   python -m venv venv

3. Activate virtual environment:
   Windows:
   venv\Scripts\activate

4. Install dependencies:
   pip install flask flask-sqlalchemy flask-cors

    What each does :
    flask → backend framework
    flask-sqlalchemy → lets Flask talk to SQLite easily
    flask-cors → allows React (frontend) to call your backend

5. Create app.py in backend

## Tech Stack

- Backend: Flask
- Frontend: React
- Database: SQLite (via SQLAlchemy)

## Features 

- Add task
- View tasks
- Mark task as complete
- Delete task
