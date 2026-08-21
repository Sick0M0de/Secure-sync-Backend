from fastapi import FastAPI
from app.database import engine, Base
from app.routers import auth, users, tasks

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SecureSync Backend",
    description="A task management API with auth",
    version="0.1.0"
)

# include routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(tasks.router)

@app.get("/")
def root():
    return {"message": "Welcome to SecureSync Backend! Check out /docs for the API."}

@app.get("/health")
def health():
    return {"status": "ok"}
