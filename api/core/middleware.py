from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from core.config import settings


class TokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        noob_token = request.headers.get('NOOB-TOKEN')
        if request.url.path == "/api/noob/health":
            response = await call_next(request)
            return response
        else:
            match noob_token:
                case settings.NOOB_TOKEN:
                    response = await call_next(request)
                    return response
                case _:
                    return JSONResponse(
                    status_code=401,
                    content={"status": "not authorized"}
                )