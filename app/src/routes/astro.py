from fastapi import APIRouter, Depends, HTTPException, UploadFile
from app.src.schemas.user import User, UserUpdate, ProfileRegister
from app.src.schemas.others import AdvertRead, ResponseRead, EmployeeRead
import app.src.crud.user as crud_user
import app.src.crud.others as crud_others
from kerykeion import KerykeionChartSVG, AstrologicalSubject
from fastapi.responses import FileResponse
from kerykeion.kr_types.kr_models import AstrologicalSubjectModel

from app.src.utils.astro import *
from app.src.utils.convert import *
from app.src.utils import DbDep
import os

router = APIRouter(prefix="/astro", tags=["astro"])

@router.get("/{simple_user_id}/")
def get_natal_by_simple_user_id(simple_user_id: int, db: DbDep) -> AstrologicalSubjectModel:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info = convert_bd_data(user.birth_date, user.birth_time)
    
    return get_natal_user_map(info)


@router.get("/{simple_user_id}/svg")
def get_natal_svg_by_simple_user_id(simple_user_id: int, db: DbDep) -> FileResponse:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info = convert_bd_data(user.birth_date, user.birth_time)
    
    file_path = get_natal_svg(info)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="image/svg+xml")
    else:
        return {"error": "SVG-файл не найден"}
    


@router.get("/{company_user_id}/")
def get_natal_by_company_user_id(company_user_id: int, db: DbDep) -> AstrologicalSubjectModel:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info = convert_bd_data(user.birth_date, user.birth_time)
    
    return get_natal_user_map(info)


@router.get("/{company_user_id}/svg")
def get_natal_svg_by_company_user_id(company_user_id: int, db: DbDep) -> FileResponse:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info = convert_bd_data(user.birth_date, user.birth_time)
    
    file_path = get_natal_svg(info)
    

# @router.get("/oftwo")
# def get_score_of_two()