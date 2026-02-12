# Todoapi

A REST API for managing users and todos. Built with FastAPI, SQLAlchemy, and PostgreSQL, it provides user registration, a simple token-authentication endpoint (a stub for now), and full CRUD for todos with owner relationships. Intended as a compact starter for local development, testing, and extension.

**Key files**
- [app.py](app.py#L1-L20): application entry, mounts routes and creates tables.
- [handlers/routes.py](handlers/routes.py#L1-L200): API routes (users, auth token, todos).
- [database/db.py](database/db.py#L1-L60): DB engine and `get_db()`.
- [database/model.py](database/model.py#L1-L200): SQLAlchemy models for `User` and `Todos`.

## Requirements
- Python 3.10+ recommended
- PostgreSQL database (the project uses a DATABASE_URL in `database/db.py`)
- Install Python deps: `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`, `pydantic` (and any others you prefer)

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
pip install fastapi uvicorn sqlalchemy psycopg2-binary
```
3. Configure the database in `database/db.py` by updating `DATABASE_URL` (example):
```
postgresql://<user>:<password>@<host>/<dbname>
```
4. Create the database in Postgres if it doesn't exist. The app will create tables automatically on startup (see [app.py](app.py#L1-L20)).
5. Run the app:
```bash
uvicorn app:app --reload
```
The API will be available at `http://127.0.0.1:8000/docs`.

## Important API endpoints (examples)
- Create user
  - POST `/Create User`
  - Body: `UserCreate` (see `database/schemas.py`)
  - Returns: `UserOut`

- Login (token)
  - POST `/token`
  - Form data: `username` (email), `password`
  - Returns: simple success string (authentication hook present)

- CRUD Todos
  - POST `/Create Todo` — create todo (body: `TodoCreate`)
  - PUT `/Update Todo` — update todo (query param `id`, body: `TodoCreate`)
  - GET `/Get All Todos` — list all todos
  - GET `/todo/{todo_id}` — get single todo
  - DELETE `/todos/{todo_id}` — delete todo
  - GET `/users/{owner_id}/todos` — todos for a user

- Users
  - GET `/users/{user_id}` — get user by id
  - GET `/Get All Users` — list users
  - DELETE `/users/{user_id}` — delete user

Note: Route names include spaces (as implemented) — keep exact paths when calling the API (e.g., `/Create Todo`).

## Database
- Postgres is used (see `database/db.py`).
- Tables are created automatically by `Base.metadata.create_all(bind=engine)` in `app.py`.


