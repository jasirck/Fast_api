from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username : str
    password : str
    place : str
    age : int

class UserCreate(UserBase):
    password : str

from pydantic import BaseModel, ConfigDict

class UserRead(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class LoginSchema(BaseModel):
    username: str
    password: str