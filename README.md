# Task-Management-System

A simple task manager that lets you add, update, view, and delete tasks. Built using **Django REST Framework (DRF)**, this application demonstrates the principles of RESTful API development.

---

## Features

- **CRUD Operations**: 
  - Create, Read, Update, and Delete tasks.
- **Task Details**: 
  - Each task includes a title, description, completion status, and timestamps.
- **RESTful Endpoints**: 
  - Organized and intuitive API endpoints for seamless integration.
- **Validation**: 
  - Ensures mandatory fields are provided and input data is valid.
- **Error Handling**: 
  - Provides meaningful error messages for invalid requests.

---

## Endpoints

| Method | Endpoint            | Description                           |
|--------|---------------------|---------------------------------------|
| GET    | `/tasks/`           | List all tasks                       |
| POST   | `/tasks/`           | Create a new task                    |
| GET    | `/tasks/<id>/`      | Retrieve a specific task by ID        |
| PUT    | `/tasks/<id>/`      | Update a task by ID (all fields)      |
| PATCH  | `/tasks/<id>/`      | Partially update a task (specific fields) |
| DELETE | `/tasks/<id>/`      | Delete a task by ID                  |

---

## Technologies Used

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, replaceable with PostgreSQL/MySQL)
- **Testing**: Postman or cURL
