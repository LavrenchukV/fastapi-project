# Internship 2025 – FastAPI Backend Project

This repository contains a backend project developed as part of the **Internship 2025** training track.  
The goal of the project is to build a complete backend environment using **Python, FastAPI, PostgreSQL (NeonDB), Alembic, Docker**, and Git, while learning professional development practices.

---

## 🚀 Project Overview

The application implements a basic **REST API** for managing users, supporting:

- Create a user  
- Retrieve all users  
- Retrieve a user by ID  
- Update a user  
- Delete a user  

Interactive API documentation (Swagger UI):

**http://localhost:8000/docs**

---

## Project Structure
```markdown
app/
├── main.py        → FastAPI entrypoint and routes
├── database.py    → SQLAlchemy engine + session + DB connection
├── models.py      → ORM models (User, etc.)
├── schemas.py     → Pydantic models for validation
├── crud.py        → All database CRUD logic
└── __init__.py    → Package marker
```

Additional project files:
- alembic/ # Alembic migrations folder
- alembic.ini # Alembic configuration file
- requirements.txt # Project dependencies
- .env # Environment variables (not included in repo)

---

## 🗄 Database Configuration

The project uses **NeonDB (PostgreSQL Cloud)**.

Database URL is stored in the `.env` file:

DATABASE_URL=postgresql+psycopg2://user:password@host/dbname

!!!!The `.env` file is excluded from the repository for security reasons.

---

## 🛠 Alembic Migrations

Alembic is used to manage database schema changes.

Completed work includes:

- Initial migration that creates the users table
- Migration adding the age field
- Full Alembic configuration (env.py, alembic.ini)
- Password hashing integration
- New migrations for product and product_details tables
- CRUD-style operations through Alembic (Create, Update, Delete)

Common commands:

```bash
alembic revision --autogenerate -m "description"
alembic upgrade head
alembic downgrade -1
```
Migrations are stored in: alembic/versions/

---

## Docker Support

The project includes a fully configured Docker environment for running the FastAPI application and applying Alembic migrations automatically.

Dockerfile key features:

- Uses python:3.11-slim as the base image
- Installs all dependencies from requirements.txt
- Copies the entire project into the container
- Automatically applies Alembic migrations on container startup
- Runs the FastAPI app using Uvicorn


Build the Docker image:
docker build -t internship-app .

Run the container with environment variables:
docker run --env-file .env -p 8000:8000 internship-app


The application will start on:

➡️ http://localhost:8000

Swagger docs:

➡️ http://localhost:8000/docs