from fastapi import APIRouter, Depends, HTTPException, status

from ...schema.userauth import UserRegisterRequest, UserLoginRequest
from ...controllers.user_auth import UserAuthController

from ...database.db import session

user_auth_router = APIRouter(prefix="/user/auth")

secret = "secret"
user_auth_controller = UserAuthController(session)


@user_auth_router.post("/register")
def register_user(user: UserRegisterRequest):
    return user_auth_controller.register_user(user)


@user_auth_router.post("/login")
def login_user(user: UserLoginRequest):
    return user_auth_controller.login_user(user)


@user_auth_router.post("/refresh")
def refresh_access_token(refresh_token: str):
    return user_auth_controller.refresh_access_token(refresh_token)
