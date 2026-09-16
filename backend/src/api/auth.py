"""
Auth endpoints. Layering: router -> service -> repository.

    POST /api/v1/auth/register  -> create account (returns user)
    POST /api/v1/auth/login     -> exchange credentials for a JWT
    GET  /api/v1/auth/me        -> return the currently authenticated user
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.models import User
from src.repositories.user_repository import UserRepository
from src.schemas.auth import Token, UserLogin, UserOut, UserRegister
from src.services.auth_service import (
    create_access_token,
    get_current_user,
    hash_password,
    verify_password,
)

router = APIRouter()


@router.post("/register", response_model=UserOut, status_code=201)
def register(data: UserRegister, db: Session = Depends(get_db)):
    """Create a new account."""
    email = data.email.strip().lower()
    if UserRepository.get_by_email(db, email):
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed = hash_password(data.password)
    return UserRepository.create(
        db,
        email=email,
        hashed_password=hashed,
        full_name=data.full_name.strip(),
        country=data.country.strip() or "Malawi",
    )


@router.post("/login", response_model=Token)
def login(data: UserLogin, db: Session = Depends(get_db)):
    """Authenticate and return a signed JWT."""
    user = UserRepository.get_by_email(db, data.email.strip().lower())
    if not user or not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    return {"access_token": create_access_token(user.id), "token_type": "bearer"}


@router.get("/me", response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    """Return the authenticated user's profile."""
    return current_user