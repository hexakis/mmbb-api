from fastapi import APIRouter
from routing.user.user import user_router
from routing.balance.balance import balance_router
from routing.noob.noob import noob_router

api_router = APIRouter()
api_router.include_router(router=user_router)
api_router.include_router(router=balance_router)
api_router.include_router(router=noob_router)