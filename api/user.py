from typing import List
from fastapi import APIRouter, Depends
from schemas.user import UserCreate , UserRead, LoginSchema, TokenSchema
from fastapi import status
import crud.user as crud
from auth import get_current_user


router = APIRouter()

@router.get("/", response_model=List[UserRead])
async def read_users(current_user: str = Depends(get_current_user)):
    print(current_user)
    return await crud.get_users()

@router.post("/signup", response_model=UserCreate, status_code=status.HTTP_201_CREATED)
async def read_users(user: UserCreate):
    return await crud.signUp_user(user)

@router.post("/signin", response_model=TokenSchema)
async def read_users(user: LoginSchema):
    return await crud.signIn_user(user)