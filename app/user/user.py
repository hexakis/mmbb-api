from fastapi import APIRouter

user_router = APIRouter(
    prefix="/user",
)

@user_router.get("/fetch")
async def fetch_user_data():
    return 

@user_router.post("/create")
async def create_new_user():
    return

@user_router.post("/delete")
async def delete_existing_user():
    return

@user_router.post("/auth")
async def authenticate_user():
    return

@user_router.post("/change")
async def change_user_data():
    return
