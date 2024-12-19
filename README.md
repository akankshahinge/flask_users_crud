# flask_users_crud
Basic Flask User's CRUD microservice

# Flask Users CRUD Application

A simple CRUD (Create, Read, Update, Delete) application built with Flask and SQLAlchemy for managing user data. The application uses PostgreSQL as the database and is containerized using Docker.

## Features

- **Create User**: Add a new user with a unique username and email.
- **Read Users**: Retrieve all users or a specific user by ID.
- **Update User**: Modify an existing user's details.
- **Delete User**: Remove a user from the database.

## Technologies Used

- **Backend**: Flask, Flask-SQLAlchemy
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose

---

## Prerequisites

- [Docker](https://www.docker.com/) installed on your system
- [Git](https://git-scm.com/) installed on your system

---

## Setup and Usage

### Clone the Repository

```
git clone https://github.com/<your-username>/flask_users_crud.git
cd flask_users_crud
```

## Build and Run the Application
Build and start the containers using Docker Compose:
```
docker-compose up --build
```
#### The Flask application will be accessible at:
http://localhost:4000
#### The PostgreSQL database will be exposed at:
localhost:5432
