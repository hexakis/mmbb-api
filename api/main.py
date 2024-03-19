from fastapi import FastAPI
from core.config import settings
from routing.base import api_router
from core.middleware import TokenMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

def include_router(app):
    app.include_router(api_router)

def include_middleware(app):
    app.add_middleware(TokenMiddleware)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    include_middleware(app)
    return app

app = start_application()
