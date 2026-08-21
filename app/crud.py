from sqlalchemy.orm import Session
from app import models, schemas
from app.auth import hash_password

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = hash_password(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Tasks
def get_user_tasks(db: Session, owner_id: int, skip=0, limit=100):
    return db.query(models.Task).filter(models.Task.owner_id == owner_id).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int, owner_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id, models.Task.owner_id == owner_id).first()

def create_task(db: Session, task: schemas.TaskCreate, owner_id: int):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        owner_id=owner_id
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate, owner_id: int):
    task = get_task(db, task_id, owner_id)
    if not task:
        return None

    # update fields if provided
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.is_completed is not None:
        task.is_completed = task_update.is_completed

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int, owner_id: int):
    task = get_task(db, task_id, owner_id)
    if not task:
        return None
    db.delete(task)
    db.commit()
    return task
