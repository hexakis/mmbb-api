from fastapi import APIRouter
from fastapi import Request

noob_router = APIRouter(
    prefix="/api",
)

@noob_router.get("/noob/health")
async def noob_health_check(request: Request):
    return {"status": "OK"}