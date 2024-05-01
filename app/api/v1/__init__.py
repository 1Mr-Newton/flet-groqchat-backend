from fastapi import APIRouter
from .user_auth import user_auth_router
from .chat import chat_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(user_auth_router)
v1_router.include_router(chat_router)
