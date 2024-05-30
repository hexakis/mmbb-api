from fastapi import FastAPI, Depends
from core.config import settings
from routing.base import api_router
from core.middleware import TokenMiddleware
from database.base import Base
from database.session import engine
from core.hashing import Hasher
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from database.session import get_db
import asyncio


def include_router(app):
    app.include_router(api_router)

def include_middleware(app):
    app.add_middleware(TokenMiddleware)
db = get_db()
def create_app() -> FastAPI:
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_middleware(app)
    include_router(app)
    return app

app = create_app()

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

class UserCreate():
    IBAN = "NL28MARB2318002966"
    firstName = "Henk"
    lastName = "Haas"
    email = "henkhaas2000@live.nl"
    phone = "+310643871012"
    birthDate = "12-03-2000"
    balance = "678"

class CardCreate():
    id = 1
    UID = 12
    expDate = "12-03-2030"
    Account_IBAN = "NL28MARB2318002966"
    pinCode = Hasher.get_password_hash("1234")

@app.on_event("startup")
async def create_bank_user():
    user = UserCreate()
    card = CardCreate()
    await db.add(user)
    await db.commit()
    await db.refresh(user)

    await db.add(card)
    await db.commit()
    await db.refresh(card)

#async def start_application():