# SecureSync Backend

A task management API built with Python and FastAPI. Users can register, login with JWT tokens, and manage their own tasks.

## Features

- User registration and login
- JWT authentication
- CRUD operations for tasks
- PostgreSQL database
- Alembic migrations
- Docker support

## Tech Stack

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Docker

## Running with Docker

```bash
docker-compose up --build
```

Then go to `http://localhost:8000/docs` to see the API docs.

## Running Locally

1. Start PostgreSQL (you can use Docker):
```bash
docker run -d --name securesync-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=securesync -p 5432:5432 postgres:16
```

2. Install dependencies:
```bash
pip install -r requirements.txt
# or
uv pip install -r requirements.txt
```

3. Run migrations:
```bash
alembic upgrade head
```

4. Start the server:
```bash
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /auth/login | Login |
| POST | /users/register | Register |
| GET | /users/me | Current user |
| GET | /users/ | All users |
| GET | /tasks/ | List tasks |
| POST | /tasks/ | Create task |
| GET | /tasks/{id} | Get task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |

## Env Variables

- `DATABASE_URL` - PostgreSQL connection string
- `SECRET_KEY` - JWT secret
- `ALGORITHM` - JWT algorithm (default HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiry

## TODO

- [ ] Add more tests
- [ ] Add password reset
- [ ] Better error handling
