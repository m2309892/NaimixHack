from app.models import user as dbu
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Union, Sequence, Type, overload
import boto3

from app.models.user import User
from app.models.config import config
from app.crud.others import get_advert_responses

s3_session = boto3.session.Session()

def get_all_users(db: Session) -> Union[list[dbu.User], None]:
    return db.scalars(select(dbu.User)).all()

#компания по айди
def get_user_by_id(db: Session, id: int) -> dbu.User | None:
    return db.get(dbu.User, id)


#компания по имейлу
def get_user_by_email(db: Session, email: str) -> dbu.User | None:
    stmt = select(dbu.User).where(dbu.User.email == email)
    return db.scalars(stmt).one_or_none()


#сотрудники компании
def get_user_employees(db: Session, id: int) -> Union[list[dbu.CompanyEmployee], None]:
    user: Type[User] | None = db.get(dbu.User, id)
    if not user:
        return None
    return user.company_emploees

#объявления компании
def get_user_adverts(db: Session, id: int) -> Union[list[dbu.Advert], None]:
    user: Type[User] | None = db.get(dbu.User, id)
    if not user:
        return None
    return user.company_adverts

#отклики на вакансии компании
def get_user_responses(db: Session, id: int) -> Union[list[dbu.Response], None]:
    user: Type[User] | None = db.get(dbu.User, id)
    if not user:
        return None
    
    adverts = get_user_adverts(db, id)
    
    ans = []
    for advert in adverts:
        responses = get_advert_responses(db, advert.id)
        for response in responses:
            ans.append(response)
            
    return ans



@overload
def create_user(db: Session, companyname: str,
                email: str,
                bio: str,
                id: str | None = None) -> dbu.User:
    ...


def create_user(db: Session, **kwargs) -> dbu.User:
    user: dbu.User = User(**kwargs)
    db.add(user)
    db.flush()
    db.commit()
    return user


@overload
def update_user(db: Session,
                id: int,
                companyname: str | None,
                email: str | None = None,
                bio: str | None = None):
    ...


def update_user(db: Session, id: int, **kwargs) -> dbu.User | None:
    _user = db.get(User, id)
    if not _user:
        return None
    for attr in kwargs.keys():
        setattr(_user, attr, kwargs[attr])
    db.flush()
    db.commit()
    return _user
    
    
# def update_user_photo(db: Session, user_id: int, photo: bytes) -> str | None:
#     s3 = s3_session.client(
#         service_name="s3",
#         region_name="ru-central1",
#         endpoint_url="https://storage.yandexcloud.net",
#         aws_access_key_id=config.ACCESS_KEY_ID,
#         aws_secret_access_key=config.SECRET_ACCESS_KEY
#     )
#     # TODO: использовать imageproxy
#     key = f"photo_{user_id}"
#     s3.put_object(Bucket=config.PHOTO_BUCKET, Key=key, Body=photo)
#     link = f"https://storage.yandexcloud.net/{config.PHOTO_BUCKET}/{key}"
#     _user = db.get(User, user_id)
#     _user.photo = link
#     db.flush()
#     db.commit()

#     return link
