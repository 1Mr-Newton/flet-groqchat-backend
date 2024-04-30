from sqlalchemy.orm import Session
from http import HTTPStatus

from ..schema.userauth import UserLoginRequest, UserRegisterRequest
from ..models.user_class import User
from ..repo.users import UserRepo
from core.exceptions.simple_exception import SimpleException


class UserAuthController:
    def __init__(self, db: Session) -> None:
        self.user_repo = UserRepo(db)

    def register_user(self, user_input: UserRegisterRequest):
        user = User(email=user_input.email, password=user_input.password)
        return self.user_repo.create_user(user)

    def login_user(self, user_input: UserLoginRequest):

        user = self.user_repo.get_user_by_email(user_input.email)
        if user and str(user.password) == user_input.password:
            return user
        raise SimpleException(
            message="Invalid credentials",
            status_code=HTTPStatus.UNAUTHORIZED,
        )
