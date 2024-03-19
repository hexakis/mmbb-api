from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session
from database.session import get_db
from pydantic import BaseModel

user_router = APIRouter(
    prefix="/user",
)

class UserCreation(BaseModel):
    firstname: str
    preposition: str
    lastname: str
    date_of_birth: str
    email: str
    phone: str 
    password: str

class UserDestruction(BaseModel):
    email: str
    password: str

@user_router.get("/fetch")
async def fetch_user_data():
    return 

@user_router.post("/create")
async def create_new_user(request: Request, user: UserCreation, db: Session = Depends(get_db)):
    return

@user_router.delete("/delete")
async def delete_existing_user(request: Request, db: Session = Depends(get_db)):
    return

@user_router.post("/auth")
async def authenticate_user(request: Request, db: Session = Depends(get_db)):
    return

@user_router.post("/change/{data}")
async def change_user_data():
    return

# f0aaf9ad-fa8b-439b-8e7f-8fc21d603dff api token