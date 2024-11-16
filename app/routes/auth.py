from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

import app.crud.user
from app.crud.user import get_user_by_email, create_user
from app.models import config

from app.utils import DbDep
from app.schemas.user import UserRegister
from app.utils.auth import authenticate_user, create_access_token, get_password_hash

router = APIRouter()

@router.post("/register")
async def register_user(
    user: UserRegister,
    db: DbDep,
):
    """
    Create a new user
    """
    db_user = get_user_by_email(db, user.email)

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )

    # is_valid_email = verify_email(user.email)

    # if not is_valid_email:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Email is not valid",
    #     )
    hash = get_password_hash(user.password)
    data = user.model_dump()
    data.pop('password')
    data['password_hash'] = hash
    user = create_user(db, **data)
    access_token_expires = timedelta(minutes=config.access_token_expire_minutes)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/login")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: DbDep,
):
    """
    we use username in OAuth2PasswordRequestForm as email
    """
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=config.access_token_expire_minutes)
    access_token = create_access_token(
        data={"email": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}