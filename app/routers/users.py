from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import schemas, crud
from app.auth import get_current_user
from app import models

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # check if username taken
    existing = crud.get_user_by_username(db, username=user.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken")

    # check email
    existing_email = crud.get_user_by_email(db, email=user.email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.create_user(db=db, user=user)
    return new_user


@router.get("/me", response_model=schemas.UserResponse)
def me(current_user: models.User = Depends(get_current_user)):
    return current_user


@router.get("/", response_model=List[schemas.UserResponse])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users
