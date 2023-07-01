from fastapi import APIRouter

from .core import router as core_router
from .post import router as post_router
from .user import router as user_router

router = APIRouter()

router.include_router(core_router, prefix="/cores", tags=["Core"])
router.include_router(post_router, prefix="/posts", tags=["Posts"])
router.include_router(user_router, prefix="/users", tags=["Users"])
