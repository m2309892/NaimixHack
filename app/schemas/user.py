from app.schemas.base import Base
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, model_validator, computed_field


class User(Base):
    id: int
    companyname: str
    email: EmailStr
    bio: str


class UserPass(User):
    password_hash: str


class UserRegister(Base):
    companyname: str
    email: EmailStr
    password: str
    bio: str = ''


class ProfileRegister(Base):
    id: int
    companyname: str
    email: EmailStr
    bio: str


class UserUpdate(Base):
    companyname: str = ''
    email: EmailStr | None
    bio: str = ''


class Token(Base):
    access_token: str
    token_type: str


class TokenData(Base):
    email: str = ''


