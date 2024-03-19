from fastapi import APIRouter
from fastapi import Request

noob_router = APIRouter(
    prefix="/noob",
)

@noob_router.get("/health")
async def noob_health_check(request: Request):
    return {"status": "OK"}
