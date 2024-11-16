from datetime import datetime
from typing import List
import enum
from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy import String, TIMESTAMP, Column, Integer, ForeignKey, Table, FetchedValue, Enum, Date, Time

from app.src.models.base import Base, HasDates




class User(Base, HasDates):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    companyname: Mapped[str] = mapped_column(String)
    bio: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password_hash: Mapped[str] = mapped_column(String)  

    teams: Mapped[List["Team"]] = relationship('Team', back_populates='user')
    company_employees: Mapped[List["CompanyEmployee"]] = relationship('CompanyEmployee', back_populates='user')
    company_adverts: Mapped[List["Advert"]] = relationship('Advert', back_populates='user')


class Team(Base):
    __tablename__ = 'teams'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    
    # Correct user_id mapping (removed primary_key=True)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  # ForeignKey relationship defined here
    company_employees: Mapped[List["CompanyEmployee"]] = relationship('CompanyEmployee', back_populates='team')
    
    # Back reference to User
    user: Mapped["User"] = relationship('User', back_populates='teams')
    
    
class Advert(Base, HasDates):
    __tablename__ = 'user_adverts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    advert_title: Mapped[str] = mapped_column(String)
    job: Mapped[str] = mapped_column(String)
    position: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))  # Corrected (removed primary_key=True)
    responses: Mapped[List["Response"]] = relationship('Response', back_populates='advert')
    
    user: Mapped["User"] = relationship('User', back_populates='company_adverts')
    
    
    
class Response(Base, HasDates):
    __tablename__ = 'responses'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    emploee_id: Mapped[int] = mapped_column(ForeignKey('simple_employees.id'))
    advert_id: Mapped[int] = mapped_column(ForeignKey('user_adverts.id'))
    
    advert: Mapped["Advert"] = relationship('Advert', back_populates='responses')
    simple_employee: Mapped["SimpleEmployee"] = relationship('SimpleEmployee', back_populates='responses')
    


    

class SimpleEmployee(Base):
    __tablename__ = 'simple_employees'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String, nullable=True)
    birth_date: Mapped[Date] = mapped_column(Date)
    birth_time: Mapped[Time] = mapped_column(Time, nullable=True)
    birth_place: Mapped[str] = mapped_column(String, nullable=True)
    resume_url: Mapped[str] = mapped_column(String, nullable=True)
    bio: Mapped[str] = mapped_column(String, nullable=True)
    
    responses: Mapped[List["Response"]] = relationship('Response', back_populates='simple_employee')
    
    
    
    
class CompanyEmployee(Base):
    __tablename__ = 'company_employees'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    surname: Mapped[str] = mapped_column(String)
    number: Mapped[str] = mapped_column(String, nullable=True)
    birth_date: Mapped[Date] = mapped_column(Date)
    birth_time: Mapped[Time] = mapped_column(Time, nullable=True)
    birth_place: Mapped[str] = mapped_column(String, nullable=True)
    resume_url: Mapped[str] = mapped_column(String, nullable=True)
    bio: Mapped[str] = mapped_column(String, nullable=True)
    
    
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    team_id: Mapped[int] = mapped_column(ForeignKey('teams.id'))
    
    
    user: Mapped["User"] = relationship('User', back_populates='company_employees')
    team: Mapped["Team"] = relationship('Team', back_populates='company_employees')