from fastapi.security import OAuth2PasswordBearer

from app.models.config import config
from app.models.user import User, Permission
from app.schemas.user import User, Token, TokenData
from app.utils import DbDep, get_db
from app.crud.user import get_user_by_email, get_user_permissions

import jwt
from functools import wraps
from passlib.context import CryptContext
from typing import Annotated
from fastapi import HTTPException, status, Depends
from datetime import datetime, timedelta, UTC
from sqlalchemy.orm import Session

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login", auto_error=False)





def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta = ''):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, config.secret_key, algorithm=config.algorithm
    )
    return encoded_jwt


def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email)
    if user is None:
        return False
    if not verify_password(password, user.password_hash):
        return False
    return user


no_token_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Not authenticated",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        db: DbDep,
) -> User | None:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    if token is None or token == "":
        return None
    try:
        payload = jwt.decode(
            token, config.secret_key, algorithms=[config.algorithm]
        )
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = get_user_by_email(db, token_data.email)
    if user is None:
        raise credentials_exception
    return user



def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user is None:
        raise no_token_exception
    return current_user

AuthDep = Annotated[User, Depends(get_current_active_user)]


# def get_current_active_admin(
#         current_user: Annotated[User, Depends(get_current_user)]
# ):
#     if current_user is None:
#         raise no_token_exception
#     if current_user.role != "admin":
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="The user doesn't have enough privileges",
#         )
#     return current_user

def check_permissions(db: Session, user: User, *perms: str):
    _perms = get_user_permissions(db, user.id)
    _exp = HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='Permission denied'
    )
    if not _perms and len(perms) > 0:
        raise _exp
    _perms = list(map(lambda p: p.name, _perms))
    for perm in perms:
        if perm not in _perms:
            raise _exp
