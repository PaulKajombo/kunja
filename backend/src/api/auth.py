from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta

from src.config import settings

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


class Token(BaseModel):
    access_token: str
    token_type: str


class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str
    country: str  # "Malawi" or "Zambia"


class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    country: str
    created_at: datetime

    class Config:
        from_attributes = True


# In-memory user store for MVP (replace with DB later)
users_db: dict[str, dict] = {}
user_counter = 0


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    global user_counter
    if user.email in users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    user_counter += 1
    users_db[user.email] = {
        "id": user_counter,
        "email": user.email,
        "password": user.password,  # TODO: hash in production
        "full_name": user.full_name,
        "country": user.country,
        "created_at": datetime.now(),
    }
    return users_db[user.email]


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    access_token = f"token-{user['id']}-{datetime.now().timestamp()}"
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme)):
    # TODO: decode JWT token in production
    return {"message": "Authenticated", "token": token}
