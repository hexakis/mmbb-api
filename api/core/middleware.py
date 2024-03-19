from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from core.config import settings


class TokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        noob_token = request.headers.get('NOOB-TOKEN')
        if noob_token == settings.NOOB_TOKEN:
            response = await call_next(request)
            return response
        else:
            return JSONResponse(
                status_code=401,
                content={"status": "not authorized"}
            )