from fastapi import APIRouter

balance_router = APIRouter(
    prefix="/balance",
)

@balance_router.post("/add")
async def add_balance():
    return 

@balance_router.post("/remove")
async def subtract_balance():
    return

@balance_router.get("/fetch")
async def fetch_balance():
    return
