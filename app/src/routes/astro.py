from fastapi import APIRouter, Depends, HTTPException, UploadFile
import app.src.utils
from app.src.schemas.user import User, UserUpdate, ProfileRegister
from app.src.schemas.others import AdvertRead, ResponseRead, EmployeeRead
import app.src.crud.user as crud_user
import app.src.crud.others as crud_others
from kerykeion import KerykeionChartSVG, AstrologicalSubject
from fastapi.responses import Response
from kerykeion.kr_types.kr_models import AstrologicalSubjectModel

from app.src.utils.astro import *
from app.src.utils.convert import *
from app.src.utils import DbDep

router = APIRouter(prefix="/astro", tags=["astro"])

@router.get("/{simple_user_id}/")
def get_natal_by_simple_user_id(simple_user_id: int, db: DbDep) -> AstrologicalSubjectModel:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    return get_natal_user_map(info)


@router.get("/{simple_user_id}/svg")
def get_natal_svg_by_simple_user_id(simple_user_id: int, db: DbDep) -> Response:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    chart_svg = get_natal_svg(info)

    return Response(content=str(chart_svg), media_type="image/svg+xml")


@router.get("/{company_user_id}/")
def get_natal_by_company_user_id(company_user_id: int, db: DbDep) -> AstrologicalSubjectModel:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    return get_natal_user_map(info)


@router.get("/{company_user_id}/svg")
def get_natal_svg_by_company_user_id(company_user_id: int, db: DbDep) -> Response:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    info = convert_bd_data(user.birth_date, user.birth_time, user.birth_place)
    
    chart_svg = get_natal_svg(info)
    
    return Response(content=str(chart_svg), media_type="image/svg+xml")

# @router.get("/")


# @router.get("/oftwo")
# def get_score_of_two()