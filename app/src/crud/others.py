from app.src.models import user as dbu
from sqlalchemy import select
from sqlalchemy.orm import Session
from typing import Union, Sequence, Type, overload, List
import boto3
from datetime import date, time

from app.src.models.user import User
from app.src.models.config import config


#COMPANYEMPLOYEE
#вытащить одного работника компании по его айди
def get_company_employee_by_id(db: Session, id: int) -> dbu.CompanyEmployee | None: 
    return db.get(dbu.CompanyEmployee, id)

@overload
def create_company_employee(db: Session, 
                user_id: int,
                name: str,
                surname: str,
                number: str | None,
                bith_date: date,
                bith_time: time | None,
                bith_place: str | None,
                resume_url: str |None,
                bio: str | None) -> dbu.CompanyEmployee:
    ...


def create_company_employee(db: Session, **kwargs) -> dbu.CompanyEmployee:
    user: dbu.CompanyEmployee = dbu.CompanyEmployee(**kwargs)
    db.add(user)
    db.flush()
    db.commit()
    return user


@overload
def update_company_employee(db: Session, 
                id: int,
                name: str | None,
                surname: str | None,
                number: str | None,
                bith_date: date | None,
                bith_time: time | None,
                bith_place: str | None,
                resume_url: str | None,
                bio: str | None):
    ...


def update_company_employee(db: Session, id: int, **kwargs) -> dbu.CompanyEmployee | None:
    _user = db.get(dbu.CompanyEmployee, id)
    if not _user:
        return None
    for attr in kwargs.keys():
        setattr(_user, attr, kwargs[attr])
    db.flush()
    db.commit()
    return _user


#TEAM
#вытащить работников команды
def get_team_employees(db: Session, team_id: int) -> Union[list[dbu.CompanyEmployee], None]:
    team: Type[dbu.Team] | None = db.get(dbu.Team, team_id)
    if not team:
        return None
    return team.company_employees

#команда по айди
def get_company_team_by_id(db: Session, id: int) -> dbu.Team| None: 
    return db.get(dbu.Team, id)

@overload
def create_company_team(db: Session, 
                user_id: int,
                name: str,
                employees: List[dbu.CompanyEmployee] | None) -> dbu.Team:
    ...


def create_company_team(db: Session, **kwargs) -> dbu.Team:
    team: dbu.Team = dbu.Team(**kwargs)
    db.add(team)
    db.flush()
    db.commit()
    return team


@overload
def update_company_team(db: Session, 
                id: int,
                name: str | None,
                employees: List[dbu.CompanyEmployee] | None):
    ...


def update_company_team(db: Session, id: int, **kwargs) -> dbu.Team | None:
    _team = db.get(dbu.Team, id)
    if not _team:
        return None
    for attr in kwargs.keys():
        setattr(_team, attr, kwargs[attr])
    db.flush()
    db.commit()
    return _team


#ADVERT
#объявление по айди
def get_company_advert_by_id(db: Session, id: int) -> dbu.Advert | None: 
    return db.get(dbu.Advert, id)


#отклики по айди объявления
def get_advert_responses(db: Session, id: int) -> Union[list[dbu.Response], None]:
    advert: Type[dbu.Advert] | None = db.get(dbu.Advert, id)
    if not advert:
        return None
    return advert.responses



@overload
def create_company_advert(db: Session, 
                user_id: int,
                advert_title: str,
                job: str,
                position: str) -> dbu.Advert:
    ...


def create_company_advert(db: Session, **kwargs) -> dbu.Advert:
    advert: dbu.Advert = dbu.Advert(**kwargs)
    db.add(advert)
    db.flush()
    db.commit()
    return advert


@overload
def update_company_employee(db: Session, 
                id: int,
                advert_title: str,
                job: str,
                position: str):
    ...


def update_company_employee(db: Session, id: int, **kwargs) -> dbu.Advert | None:
    _advert = db.get(dbu.Advert, id)
    if not _advert:
        return None
    for attr in kwargs.keys():
        setattr(_advert, attr, kwargs[attr])
    db.flush()
    db.commit()
    return _advert


#RESPONSE
#отклик по айди
def get_response_by_id(db: Session, id: int) -> dbu.Response | None: 
    return db.get(dbu.Response, id)


#работник по айди отклика
def get_response_employees(db: Session, id: int) -> Union[list[dbu.SimpleEmployee], None]: 
    response: Type[dbu.Response] | None = db.get(dbu.Response, id)
    if not response:
        return None
    return response.emploee_id

@overload
def create_company_response(db: Session,
                            employee_id: int,
                            advrt_id: int) -> dbu.Response:
    ...


def create_company_response(db: Session, **kwargs) -> dbu.Response:
    response: dbu.Response = dbu.Response(**kwargs)
    db.add(response)
    db.flush()
    db.commit()
    return response



#SIMPLEEMPLOYEE
#работник по айди
def get_simple_employee_by_id(db: Session, id: int) -> dbu.SimpleEmployee | None: 
    return db.get(dbu.SimpleEmployee, id)


#ALLEMPLOYEES
#дата рождения по айди работника 
def get_date(db: Session, id: int) ->  date:
    user = db.query(dbu.Emplpoyee).filter(dbu.Emplpoyee.id == id).one()
    return user.birth_date


#время рождения по айди работника 
def get_date(db: Session, id: int) ->  time:
    user = db.query(dbu.Emplpoyee).filter(dbu.Emplpoyee.id == id).one()
    return user.birth_time


#место рождения по айди работника 
def get_date(db: Session, id: int) ->  str:
    user = db.query(dbu.Emplpoyee).filter(dbu.Emplpoyee.id == id).one()
    return user.birth_place



