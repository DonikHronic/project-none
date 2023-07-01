from fastapi import APIRouter

from apps.api import router as api_router

router = APIRouter()

router.include_router(api_router, prefix="/api", tags=["API"])
