from fastapi import FastAPI
from core.config import settings
from routing.base import api_router
from core.middleware import TokenMiddleware
from database.base import Base
from database.session import engine

def include_router(app):
    app.include_router(api_router)

def include_middleware(app):
    app.add_middleware(TokenMiddleware)

def create_tables():
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    include_middleware(app)
    create_tables()
    return app

app = start_application()
