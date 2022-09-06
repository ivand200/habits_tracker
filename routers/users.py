import logging
import sys
from typing import List, Dict

from fastapi import APIRouter, status, Depends, HTTPException, Header, Response
from motor.motor_asyncio import AsyncIOMotorDatabase

from models.users import UserPublic, UserCreate, UserLogin, UserDB
from db import get_database
from .auth import pwd_context, JWT_ALGORITHM, JWT_SECRET

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)




router = APIRouter()


async def get_user_or_404(
    user: UserLogin, database: AsyncIOMotorDatabase = Depends(get_database)
) -> UserDB:
    """
    Get user from db or 404
    """




async def check_user(
    email: str, database: AsyncIOMotorDatabase = Depends(get_database)
) -> UserDB:
    """
    Check existing user
    """
    get_user = await database.users.find_one({"email": email})
    if get_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"User with email: {email} already exists.",
        )
    return get_user


@router.post(
    "/registration", response_model=UserPublic, status_code=status.HTTP_201_CREATED
)
async def new_user_reg(
    user: UserCreate, database: AsyncIOMotorDatabase = Depends(get_database)
) -> UserPublic:
    """
    New user registration
    TODO: email verification, verification code
    """
    logger.info(f"Registration user email: {user.email} | username: {user.username}")
    user_db = await check_user(user.email, database)
    hashed_password = pwd_context.hash(user.password)
    new_user = await database.users.insert_one(
        {
            "username": user.username,
            "email": user.email,
            "password": hashed_password,
            "varified": False,
        }
    )
    refresh_user = await database.users.find_one({"email": user.email})
    return refresh_user


# @router.post("/confirm", status_code=status.HTTP_200_OK)
# async def code_confirm():
#     """
#     Confirmation
#     """


# @router.post("/resend", status_code=status.HTTP_200_OK)
# async def code_resend():
#     """
#     Resend confirmation code
#     """


@router.post("/login", status_code=status.HTTP_200_OK)
async def user_login(
    user: UserLogin, database: AsyncIOMotorDatabase = Depends(get_database)
) -> str:
    """
    User login by email, password
    """
    user_db = await database.users.find_one({"email": user.email})
    if user_db is None:
        raise HTTPException(status_code=404, detail="Not Found")
    verify_password = pwd_context.verify(user.password, user_db["password"])
    if not verify_password:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return "token"




# @router.post("/refresh-token", status_code=status.HTTP_200_OK)
# async def refresh_token(token: str) -> str:
#     """
#     Refresh token
#     """


# @router.get("/user", status_code=status.HTTP_200_OK)
# async def get_user_info(
#     token: str,
#     database: AsyncIOMotorDatabase = Depends(get_database),
# ) -> Dict:
#     """
#     Get user info by user
#     """


# @router.put("/user", status_code=status.HTTP_200_OK)
# async def user_update(
#     token: str,
#     database: AsyncIOMotorDatabase = Depends(get_database),
# ) -> Dict:
#     """
#     Update user info
#     """


# @router.delete("/user", status_code=status.HTTP_200_OK)
# async def delete_user(
#     token: str,
#     database: AsyncIOMotorDatabase = Depends(get_database),
# ) -> Dict:
#     """
#     Delete user
#     TODO: email verification code
#     """


# @router.post("/user/password", status_code=status.HTTP_200_OK)
# async def password_reset():
#     """
#     Password reset
#     TODO: email verification, verification code
#     """
