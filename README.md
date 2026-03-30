# Todo App (Flask + React + SQLite)

A simple full-stack Todo application built with Flask (backend), React (frontend), and SQLite (database).

## Project Structure

```text
todo-app/
├── backend/
├── frontend/
```

## Backend Setup (One-Time)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install flask flask-sqlalchemy flask-cors
```

## Frontend Setup (One-Time)

```bash
cd frontend
npm install
```

## Run the App (After Initial Setup)

### Start Backend

```bash
cd backend
venv\Scripts\activate   # Windows
python app.py
```

### Start Frontend

```bash
cd frontend
npm start
```

### Access the App

- Frontend: http://localhost:3000  
- Backend API: http://127.0.0.1:5000  

## API Endpoints

- `GET /tasks` → Fetch all tasks  
- `POST /tasks` → Create a new task  
- `PUT /tasks/<id>` → Update task status  
- `DELETE /tasks/<id>` → Delete a task 

## Tech Stack

- Backend: Flask
- Frontend: React
- Database: SQLite (via SQLAlchemy)

## Features 

- Add task
- View tasks
- Mark task as complete
- Delete task
