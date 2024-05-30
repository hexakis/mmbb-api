from fastapi import FastAPI, Depends, HTTPException, Query, Request, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from datetime import datetime
from database.models.users import User
from database.models.cards import Cards
from database.session import get_db
from core.hashing import Hasher

router = APIRouter(
    prefix="/api",
)

db = get_db()

class accountJSON(BaseModel):
    target: str
    pincode: int
    uid: str

class withdrawJSON(BaseModel):
    amount: int
    target: str
    pincode: str
    uid: str

@router.get("/noob/health")
async def noob_health_check(request: Request):
    return {"status": "OK"}

@router.post("/accountinfo")
async def fetch_account_info(request: Request, json: accountJSON, db: AsyncSession = Depends(get_db)):
    try:
        user_result = await db.execute(select(User).where(User.IBAN == json.target))
        user = user_result.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404)

        card_result = await db.execute(select(Cards).where(Cards.Account_IBAN == json.target, Cards.UID == json.uid))
        card = card_result.scalar_one_or_none()
        if card is None:
            raise HTTPException(status_code=404)

        pincode = Hasher.verify_password(json.pincode, card.pinCode)
        if pincode is False:
            raise HTTPException(status_code=401)

        return {"firstname": user.firstName, "lastname": user.lastName, "balance": user.balance}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500)


@router.post("/withdraw")
async def withdraw_money(request: Request, json: withdrawJSON, db: AsyncSession = Depends(get_db)):
    if json.amount > 200:
        raise HTTPException(status_code=400)
    if json.amount <= 0:
        raise HTTPException(status_code=400)

    try:
        user_result = await db.execute(select(User).where(User.IBAN == json.target))
        user = user_result.scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404)

        card_result = await db.execute(select(Cards).where(Cards.Account_IBAN == json.target, Cards.UID == json.uid))
        card = card_result.scalar_one_or_none()
        if card is None:
            raise HTTPException(status_code=404)

        pincode = Hasher.verify_password(json.pincode, card.pinCode)
        if pincode is False:
            raise HTTPException(status_code=401)

        if user.balance < json.amount:
            raise HTTPException(status_code=412)

        user.balance -= request.amount

        await db.commit()
        await db.refresh(user)
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        raise HTTPException(status_code=500)

    return {"status": "Success"}
