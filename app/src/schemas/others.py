from app.src.schemas.base import Base
from datetime import datetime
import re 
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator, model_validator, computed_field
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import date, time


from kerykeion import KerykeionChartSVG, AstrologicalSubject


# Схема для Employee
class EmployeeBase(BaseModel):
    name: str
    surname: str
    number: str | None = None
    birth_date: date 
    birth_time: time | None = None
    birth_place: str | None = None
    resume_url: Optional[str] = None
    bio: str | None = None
    
    # @field_validator("number")
    # def validate_phone_number(cls, value: str) -> str:
    #     if not re.match(r'^\+\d{5,15}$', value):
    #         raise ValueError('Номер телефона должен начинаться с "+" и содержать от 5 до 15 цифр')
    #     return value
    

class EmployeeCreate(EmployeeBase):
    pass  # Можно добавить дополнительные поля для создания

class EmployeeRead(EmployeeBase):
    id: int



class EmployeeUpdate(BaseModel):
    name: Optional[str]
    surname: Optional[str]
    number: Optional[str]
    birth_date: Optional[date]
    birth_time: Optional[time]
    birth_place: Optional[str]
    resume_url: Optional[str]
    bio: Optional[str]
    

# Схема для Team
class TeamBase(BaseModel):
    name: str
    

class TeamCreate(TeamBase):
    user_id: int


class TeamRead(TeamBase):
    id: int
    user_id: int


class TeamUpdate(BaseModel):
    name: Optional[str]


# Схема для CompanyEmployee
class CompanyEmployeeBase(EmployeeBase):
    user_id: int 
    team_id: Optional[int]


class CompanyEmployeeCreate(CompanyEmployeeBase):
    pass


class CompanyEmployeeRead(CompanyEmployeeBase):
    id: int


class CompanyEmployeeUpdate(EmployeeUpdate):
    user_id: Optional[int]
    team_id: Optional[int]


# Схема для Advert
class AdvertBase(BaseModel):
    advert_title: str
    job: str
    position: str
    description: str


class AdvertCreate(AdvertBase):
    user_id: int


class AdvertRead(AdvertBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class AdvertUpdate(BaseModel):
    advert_title: Optional[str]
    job: Optional[str]
    position: Optional[str]
    description: Optional[str]


# Схема для Response
class ResponseBase(BaseModel):
    emploee_id: int
    advert_id: int


class ResponseCreate(ResponseBase):
    pass


class ResponseRead(ResponseBase):
    id: int

    class Config:
        orm_mode = True



class ResponseUpdate(BaseModel):
    emploee_id: Optional[int]
    advert_id: Optional[int]

