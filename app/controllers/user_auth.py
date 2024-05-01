import jwt
import datetime
from sqlalchemy.orm import Session
from http import HTTPStatus

from core.security.jwt_handler import JWTHandler
from core.exceptions.simple_exception import SimpleException

from ..schema.userauth import UserAuthResponse, UserLoginRequest, UserRegisterRequest
from ..models.user_class import User
from ..repo.users import UserRepo


class UserAuthController:
    def __init__(self, db: Session) -> None:
        self.user_repo = UserRepo(db)

    def generate_access_token(self, user_id: str):
        expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=15)
        payload = {"user_id": user_id, "exp": expiration_time, "type": "access"}

        return JWTHandler.encode(payload)

    def generate_refresh_token(self, user_id: str):
        expiration_time = datetime.datetime.now() + datetime.timedelta(days=30)
        payload = {"user_id": user_id, "exp": expiration_time, "type": "refresh"}

        return JWTHandler.encode(payload)

    def register_user(self, user_input: UserRegisterRequest) -> UserAuthResponse:
        user = User(email=user_input.email, password=user_input.password)
        user = self.user_repo.create_user(user)

        access_token = self.generate_access_token(str(user.id))
        refresh_token = self.generate_refresh_token(str(user.id))
        return UserAuthResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=15,
        )

    def login_user(self, user_input: UserLoginRequest) -> UserAuthResponse:
        user = self.user_repo.get_user_by_email(user_input.email)
        if user and str(user.password) == user_input.password:
            access_token = self.generate_access_token(str(user.id))
            refresh_token = self.generate_refresh_token(str(user.id))
            return UserAuthResponse(
                access_token=access_token,
                refresh_token=refresh_token,
                expires_in=15,
            )

        raise SimpleException(
            message="Invalid credentials",
            status_code=HTTPStatus.UNAUTHORIZED,
        )

    def refresh_access_token(self, refresh_token: str) -> UserAuthResponse:
        payload = JWTHandler.decode(refresh_token)
        if payload["type"] != "refresh":
            raise SimpleException(
                message="Invalid token",
                status_code=HTTPStatus.UNAUTHORIZED,
            )
        user_id = payload["user_id"]
        access_token = self.generate_access_token(user_id)
        refresh_token = self.generate_refresh_token(user_id)
        return UserAuthResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in=15,
        )
