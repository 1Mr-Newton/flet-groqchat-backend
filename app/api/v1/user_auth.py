from fastapi import APIRouter, Depends, HTTPException, status

from ...schema.userauth import UserRegisterRequest
from ...controllers.user_auth import UserAuthController

from ...database.db import session

user_auth_router = APIRouter(prefix="/user/auth")


user_auth_controller = UserAuthController(session)


@user_auth_router.post("/register")
def register_user(user: UserRegisterRequest):
    return user_auth_controller.register_user(user)
