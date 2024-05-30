from fastapi import APIRouter
from routing.noob.noob import router

api_router = APIRouter()
api_router.include_router(router=router)