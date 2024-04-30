from pydantic import BaseModel, UUID4, EmailStr


class UserRegisterRequest(BaseModel):

    email: EmailStr
    password: str


class UserLoginRequest(BaseModel):
    email: str
    password: str


class UserAuthResponse(BaseModel):
    access_token: str
    refresh_token: str
    expires_in: int
