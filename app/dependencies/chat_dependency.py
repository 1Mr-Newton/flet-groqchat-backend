from http import HTTPStatus
from typing import Annotated

from fastapi import Header
from core.exceptions.simple_exception import SimpleException
from core.security.jwt_handler import JWTHandler


# async def chat_token_dependency(
#     request: AdminRequest, authorization: Annotated[str, Header()]
# ):
#     if authorization:
#         decoded_token = JWTHandler.decode(authorization)
#         if "id" in decoded_token:
#             request.admin_id = decoded_token["id"]
#             admin_profile = admin_profile_repo.by_admin_id(decoded_token["id"])
#             request.admin_profile_id = admin_profile["id"]
#             return

#         raise SimpleException(
#             status_code=HTTPStatus.UNAUTHORIZED,
#             message="User not authorized",
#         )
