from datetime import datetime, timedelta
from jose import jwt, JWTError, ExpiredSignatureError
from typing import Any
from core.env_settings import EnvironmentSettings
from fastapi import HTTPException
from http import HTTPStatus
from core.exceptions.simple_exception import SimpleException


class JWTHandler:
    __algorithmn = "HS256"

    @staticmethod
    def encode(payload: dict) -> str:
        return jwt.encode(
            payload,
            EnvironmentSettings.TOKEN_SECRET,
            algorithm=JWTHandler.__algorithmn,
        )

    @staticmethod
    def decode(token: str) -> dict[str, Any]:
        if token:
            try:
                return jwt.decode(
                    token=token,
                    key=EnvironmentSettings.TOKEN_SECRET,
                    algorithms=JWTHandler.__algorithmn,
                    options={"verify_aud": False},
                )
            except ExpiredSignatureError:
                raise SimpleException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    message="Token has expired",
                )
            except JWTError as e:
                raise SimpleException(
                    status_code=HTTPStatus.UNAUTHORIZED,
                    message="Token error ",
                )
        raise SimpleException(
            status_code=HTTPStatus.UNAUTHORIZED,
            message="Invalid token was provided",
        )
