from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

app.include_router(products_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
