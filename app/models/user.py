from datetime import datetime
from typing import List
import enum
from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, TIMESTAMP, Column, Integer, ForeignKey, Table, FetchedValue, Enum, Date, Time

from app.models.base import Base, HasDates


class Emplpoyee(Base):
    __tablename__ = 'employees'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String)
    birth_date: Mapped[Date] = mapped_column(Date)
    birth_time: Mapped[Time] = mapped_column(Time)
    birth_place: Mapped[str] = mapped_column(String)
    resume_url: Mapped[str] = mapped_column(String, nullable=True)
    bio: Mapped[str] = mapped_column(String)
    _type: Mapped[str] = mapped_column(String)
    
    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': '_type'
    }




class User(Base, HasDates):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    companyname: Mapped[str] = mapped_column(String)
    bio: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password_hash: Mapped[str] = mapped_column(String)  
    logo: Mapped[str] = mapped_column(String, nullable=True)

    teams: Mapped[List["Team"]] = relationship(secondary='teams', back_populates='users')
    company_emploees: Mapped[List["CompanyEmployee"]] = relationship(secondary='company_employees', back_populates='users')
    company_adverts: Mapped[List["Advert"]] = relationship(secondary='user_adverts', back_populates='users')


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

    company_employees: Mapped[List["CompanyEmployee"]] = relationship(secondary='company_employees', back_populates='teams')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)


class CompanyEmployee(Emplpoyee):
    __tablename__ = 'company_employees'
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'), primary_key=True)
    
    _type: Mapped[str] = mapped_column(String)
    
    __mapper_args__ = {
        'polymorphic_identity': 'company_employee',
    }
    
    
class Advert(Base, HasDates):
    __tablename__ = 'user_adverts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    advert_title: Mapped[str] = mapped_column(String)
    job: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    
    responses: Mapped[List["Response"]] = relationship(secondary='responses', back_populates='adverts')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), primary_key=True)
    
    
class Response(Base, HasDates):
    __tablename__ = 'responses'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    emploee_id: Mapped[int] = mapped_column(ForeignKey('simple_employees.id'), primary_key=True)
    advert_id: Mapped[int] = mapped_column(ForeignKey('adverts.id'), primary_key=True)
    

class SimpleEmployee(Emplpoyee):
    __tablename__ = 'simple_employees'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    responses: Mapped[List["Response"]] = relationship(secondary='responses', back_populates='simple_employees')
    _type: Mapped[str] = mapped_column(String)
    
    __mapper_args__ = {
        'polymorphic_identity': 'simple_employee'
    }