import json
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from config.settings import app_settings
from src.infrastructure.middleware import UUIDMiddleware
from src.routers.products import router as products_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    The lifespan of the application.

    This is an async context manager.
    Called at application startup and shutdown.
    """

    # Startup event
    print("Starting application")
    yield
    # Shutdown event
    print("Shutting down application")


app = FastAPI(
    debug=app_settings.DEBUG,
    lifespan=lifespan,
    redirect_slashes=False,
    title=app_settings.APP_NAME,
    version=app_settings.APP_VERSION,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=app_settings.CORS_ALLOWED_ORIGINS,
    allow_methods=app_settings.CORS_ALLOWED_METHODS,
    allow_headers=app_settings.CORS_ALLOWED_HEADERS,
)

app.add_middleware(UUIDMiddleware)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    This exception handler catches StarletteHTTPException exceptions and returns a JSONResponse
    with a status code and a JSON body containing the error detail.

    :param request: The incoming request
    :param exc: The StarletteHTTPException exception
    :return: A JSONResponse with a status code and a JSON body containing the error detail
    """

    return JSONResponse(
        status_code=exc.status_code,
        content=json.loads(exc.detail),
    )


app.include_router(products_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
