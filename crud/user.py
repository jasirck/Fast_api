from database import database
from models.user import users
from schemas.user import UserCreate, UserRead,LoginSchema
from fastapi import HTTPException
from security import get_password_hash, verify_password
from auth import create_access_token, create_refresh_token, verify_token
from pydantic import BaseModel



async def get_users() -> UserRead:
    query = users.select()
    user_list = await database.fetch_all(query)
    return [ dict(user) for user in user_list]

async def signUp_user(user: UserCreate) -> UserRead:
    quary = users.select().where(users.c.username == user.username)
    existing_user = await database.fetch_one(quary)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(user.password)
    query = users.insert().values(username=user.username, password=hashed_password, place=user.place, age=user.age)
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}

async def signIn_user(user: LoginSchema) :
    quary = users.select().where(users.c.username == user.username) 
    existing_user = await database.fetch_one(quary)
    if not existing_user:
         raise HTTPException(status_code=400, detail="User not found")
    if not verify_password(user.password, existing_user['password']):
        raise HTTPException(status_code=400, detail="Incorrect password")
    payload = {"sub": user.username}
    access_token = create_access_token(payload)
    refresh_token = create_refresh_token(payload)
    return {"access_token": access_token,"refresh_token": refresh_token,"token_type": "bearer"}
       

