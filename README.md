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
.
├── app/                               # Main FastAPI application package
│   ├── main.py                        # Application entrypoint (FastAPI instance, routers)
│   ├── database.py                    # Database engine, SessionLocal, and connection setup
│   ├── models.py                      # SQLAlchemy ORM models (User, Product, etc.)
│   ├── schemas.py                     # Pydantic schemas for request/response validation
│   ├── crud.py                        # CRUD operations and business logic accessing the DB
│   ├── security.py                    # Password hashing and authentication utilities
│   └── __init__.py
│
├── alembic/                           # Alembic migrations directory
│   ├── versions/                      # Auto-generated migration revision files
│   ├── env.py                         # Alembic environment and metadata configuration
│   └── script.py.mako                 # Template for generating new migration files
│
├── .github/                           # GitHub-based automation (CI/CD)
│   └── workflows/
│       └── ci.yml                     # GitHub Actions pipeline (runs migrations + tests)
│
├── alembic.ini                        # Main Alembic configuration file
├── requirements.txt                   # Python dependencies for the project
├── Dockerfile                         # Docker image build instructions for FastAPI app
├── .dockerignore                      # Files excluded from Docker build context
├── .env.example                       # Template for environment variables
├── .env                               # Local environment variables (not committed to Git)
├── .gitignore                         # Files and folders excluded from Git version control
└── README.md                          # Project documentation and usage instructions
```

Additional project files:

- alembic/ — Alembic migrations folder
- alembic.ini — Alembic configuration file
- requirements.txt — Project dependencies (pip freeze)
- .env — Environment variables (not included in repo)
- .env.example — Template for environment variables
- Dockerfile — Docker image build configuration
- .dockerignore — Ignore rules for Docker build context
- .gitignore — Files excluded from source control
- .github/workflows/ci.yml — Continuous Integration pipeline (runs Alembic migrations and tests)
- README.md — Project description and documentation

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

CI Migration Verification

All Alembic migrations are automatically executed inside the GitHub Actions pipeline, ensuring schema consistency and preventing broken revisions.
This guarantees migration integrity on every commit.

---

## Continuous Integration (CI) – GitHub Actions

This project includes a CI pipeline using GitHub Actions, which automatically runs on each push or pull request to the main branch.

🔧 What the CI pipeline does:

- Sets up a fresh Ubuntu environment
- Installs Python and all dependencies
- Starts a temporary PostgreSQL database using a Docker service
- Exposes the database through the environment variable DATABASE_URL
- Applies all Alembic migrations automatically:
- alembic upgrade head
- Runs all automated tests (pytest)

This ensures that:

- Migrations always work on a clean database
- The application structure stays stable
- Code is validated before merging into main

CI file location:
.github/workflows/ci.yml

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

CI/CD Note

Docker is used locally for development, while GitHub Actions uses a lightweight PostgreSQL Docker service for schema validation and automated tests.
The application container itself is not yet built or deployed in CI (deployment automation may be added in future stages).
