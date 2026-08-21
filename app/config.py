import os

# TODO: move these to .env properly later
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/securesync")
SECRET_KEY = os.getenv("SECRET_KEY", "my-super-secret-key-123")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
