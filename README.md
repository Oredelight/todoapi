# TodoAPI

TodoAPI is a RESTful web service for managing users and their todo tasks. Built with FastAPI, SQLAlchemy, and PostgreSQL, it provides robust user authentication, secure password hashing, and full CRUD operations for todos. This project is ideal for learning, local development, and as a foundation for more advanced applications.

## Features
- User registration and login with hashed passwords
- JWT-based authentication (token generation)
- CRUD operations for todos, linked to users
- PostgreSQL database integration
- Automatic table creation on startup
- Clean, modular code structure

## Project Structure

- [app.py](app.py): Application entry point; initializes FastAPI, mounts routes, and creates tables.
- [handlers/routes.py](handlers/routes.py): Defines all API endpoints for users, authentication, and todos.
- [handlers/auth.py](handlers/auth.py): Handles JWT token creation and authentication logic.
- [database/db.py](database/db.py): Sets up the database engine, session, and base model.
- [database/model.py](database/model.py): SQLAlchemy models for `User` and `Todos` tables.
- [database/schemas.py](database/schemas.py): Pydantic schemas for request/response validation.
- [database/user.py](database/user.py): User-related database operations (create, get, delete, authenticate).
- [database/todo.py](database/todo.py): Todo-related database operations (create, update, delete, get).

## Requirements
- Python 3.10 or higher
- PostgreSQL database server
- Recommended packages: `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, `pydantic`, `python-jose`, `passlib`


## Quickstart (development)
1. Create and activate a virtualenv:
  ```bash
  python -m venv .venv
  # Windows PowerShell
  .\.venv\Scripts\Activate
  # cmd
  .\.venv\Scripts\activate
  ```
2. Install dependencies:
  ```bash
  pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose passlib pydantic
  ```
3. Configure the database in `database/db.py` by updating `DATABASE_URL` (example):
  ```python
  DATABASE_URL = "postgresql://<user>:<password>@<host>/<dbname>"
  ```
  Create the database in Postgres if it doesn't exist. The app will create tables automatically on startup.
4. Run the app:
  ```bash
  uvicorn app:app --reload
  ```
  The API will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## API Endpoints



### User Endpoints

- **Register User**
  - `POST /register_user`
  - Request body: `{ "email": str, "username": str, "password": str (min 8 chars) }`
  - Response: `{ "id": int, "email": str, "created_at": str }`

- **Login**
  - `POST /login`
  - Request body: `{ "email": str, "password": str }`
  - Response: `{ "access_token": str, "token_type": "bearer" }`

- **Get User by ID**
  - `GET /users/{user_id}`
  - Response: `{ "id": int, "email": str, "created_at": str }`

- **Get All Users**
  - `GET /users`
  - Response: List of users (`UserOut`)

- **Delete User**
  - `DELETE /users/{user_id}`
  - Response: `{ "message": "User deleted succcessfully" }`

- **Get Todos by User**
  - `GET /users/{owner_id}/todos`
  - Response: List of todos for the user (`TodoOut`)

### Todo Endpoints

- **Create Todo**
  - `POST /create_todo`
  - Request body: `{ "description": str, "status": str, "owner_id": int }`
  - Response: `TodoOut`

- **Update Todo**
  - `PUT /update_todo/{todo_id}`
  - Request body: `{ "description": str, "status": str, "owner_id": int }`
  - Response: Updated `TodoOut`

- **Get All Todos**
  - `GET /todos`
  - Response: List of `TodoOut`

- **Get Todo by ID**
  - `GET /todo/{todo_id}`
  - Response: `TodoOut`

- **Delete Todo**
  - `DELETE /todos/{todo_id}`
  - Response: `{ "message": "Todo deleted successfully" }`


## Authentication
- Passwords are securely hashed using `passlib` (bcrypt).
- JWT tokens are generated for login using `python-jose`.
- Endpoints are not protected by default, but you can extend the code to require authentication for sensitive routes.


## Database
- Uses PostgreSQL (configure in `database/db.py`).
- Tables are created automatically on app startup via `Base.metadata.create_all(bind=engine)`.
- Models:
  - **User**: `id`, `username`, `email`, `hashed_password`, `created_at`
  - **Todos**: `id`, `description`, `status`, `owner_id`, `created_at`, `updated_at`


## Example Request Bodies

**UserCreate**
```json
{
  "email": "user@example.com",
  "username": "user1",
  "password": "yourpassword"
}
```

**TodoCreate**
```json
{
  "description": "Buy groceries",
  "status": "pending",
  "owner_id": 1
}
```
  - Form data: `username` (email), `password`

  - Returns: simple success string (authentication hook present)

