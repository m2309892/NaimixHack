from fastapi import APIRouter, Depends, HTTPException, UploadFile
import app.utils
from app.schemas.user import User, UserUpdate, ProfileRegister
from app.schemas.others import AdvertRead, ResponseRead, EmployeeRead
import app.crud.user as crud_user
import app.crud.others as crud_others
from kerykeion import KerykeionChartSVG, AstrologicalSubject

from app.utils.astro import *
from app.utils.convert import *

router = APIRouter(prefix="/astro", tags=["astro"])

@router.get("/{simple_user_id}/")
def get_natal_by_simple_user_id(simple_user_id: int, db: app.utils.DbDep) -> AstrologicalSubject:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    return get_natal_user_map(info)


@router.get("/{simple_user_id}/svg")
def get_natal_svg_by_simple_user_id(simple_user_id: int, db: app.utils.DbDep) -> KerykeionChartSVG:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    return get_natal_svg(info)


@router.get("/{company_user_id}/")
def get_natal_by_company_user_id(company_user_id: int, db: app.utils.DbDep) -> AstrologicalSubject:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    return get_natal_user_map(info)


@router.get("/{company_user_id}/svg")
def get_natal_svg_by_company_user_id(company_user_id: int, db: app.utils.DbDep) -> KerykeionChartSVG:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    return get_natal_svg(info)

# @router.get("/")


# @router.get("/oftwo")
# def get_score_of_two()