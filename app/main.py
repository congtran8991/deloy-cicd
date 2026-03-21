from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import api_router
from app.middleware.cors import add_cors_middleware

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="A modern FastAPI application",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Middleware
add_cors_middleware(app)

# Include API routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "version": settings.APP_VERSION,
        "docs": "/docs",
    }


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy"}
