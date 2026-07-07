#explains the project

# FastAPI Capstone

## Overview

This project is a simple FastAPI application created as part of the Week 3 Capstone.

It demonstrates:
- FastAPI Basics
- GET API
- POST API
- Pydantic Models
- Swagger Documentation

---

## Project Structure

```
fastapi-capstone/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── models.py
│   └── database.py
│
├── requirements.txt
└── README.md
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn app.main:app --reload
```
#uvicorn = the server that runs the application
#reload = so need of manually start the server
---

## API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

---

## Available APIs

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home endpoint |
| POST | /user | Create a new user |
| GET | /users | Get all users |

---

## Author

Trushna Savale