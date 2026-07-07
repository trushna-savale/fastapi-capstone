#API endpoints (GET,POST,PUT)
from fastapi import APIRouter
from app.models import User

router = APIRouter()

users = []

@router.get("/")
def home():
    return {"message": "Welcome"}

@router.post("/user")
def create_user(user: User):
    users.append(user)
    return user

@router.get("/users")
def get_users():
    return users
#APIRouter() because it only defines routes