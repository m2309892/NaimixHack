from fastapi import APIRouter, Depends, HTTPException, UploadFile
import app.src.crud.user as crud_user
import app.src.crud.others as crud_others
from fastapi.responses import FileResponse
from kerykeion.kr_types.kr_models import AstrologicalSubjectModel
from typing import Dict, Tuple, List

from app.src.utils.astro import *
from app.src.utils.convert import *
from app.src.utils import DbDep
from app.src.crud.others import *
from app.src.analitics.one_to_all import one_to_all, all_percentage
from app.src.analitics.team_select import team_select
from app.src.analitics.sup_func import weights_normalization, team_percentage
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
def get_natal_svg_by_simple_user_id(simple_user_id: int, db: DbDep) -> Dict[str, str] | str:
    user = crud_others.get_simple_employee_by_id(db, simple_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info = convert_bd_data(user.birth_date, user.birth_time)
    
    file_path = get_natal_svg(info)
    if os.path.exists(file_path):
        return file_path
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
def get_natal_svg_by_company_user_id(company_user_id: int, db: DbDep) -> Dict[str, str] | str:
    user = crud_others.get_company_employee_by_id(db, company_user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info = convert_bd_data(user.birth_date, user.birth_time)
    
    file_path = get_natal_svg(info)
    if os.path.exists(file_path):
        return file_path
    else:
        return {"error": "SVG-файл не найден"}



@router.get("/of_new_and_company_employee/")
def get_score_of_two_diff(company_emp_id: int, new_emp_id: int, db: DbDep) -> int:
    user1 = crud_others.get_company_employee_by_id(db, company_emp_id)
    user2 = crud_others.get_simple_employee_by_id(db, new_emp_id)
    
    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info1 = convert_bd_data(user1.birth_date, user1.birth_time)
    info2 = convert_bd_data(user2.birth_date, user2.birth_time)
    
    return get_score(info1, info2)
    
    
    
    
@router.get("/of_two_company_employees/")
def get_score_of_two_same(emp1_id: int, emp2_id, db: DbDep) -> int:
    user1 = crud_others.get_company_employee_by_id(db, emp1_id)
    user2 = crud_others.get_company_employee_by_id(db, emp2_id)
    
    if not user1 or not user2:
        raise HTTPException(status_code=404, detail="Response not found")
    
    info1 = convert_bd_data(user1.birth_date, user1.birth_time)
    info2 = convert_bd_data(user2.birth_date, user2.birth_time)
    
    return get_score(info1, info2)
    
    
    
def get_params_of_team_and_employee(team_id: int, simple_employee_id: int, db: DbDep):
    list1 = crud_others.get_team_employees(db, team_id)
    new = crud_others.get_simple_employee_by_id(db, simple_employee_id)
    
    employee = {new.id: new.name}
    names = {}
    team = []
    memb = []
    
    
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            s = get_score(convert_bd_data(list1[i].birth_date, list1[i].birth_time), convert_bd_data(list1[j].birth_date, list1[j].birth_time))
            t = tuple[list1[i].id, list1[j].id, s]
            team.append(t)
    
    
    for emp in list1:
        names[emp.id] = emp.name
        s = get_score(convert_bd_data(emp.birth_date, emp.birth_time), convert_bd_data(new.birth_date, new.birth_time))
        t1 = tuple[emp.id, new.id, s]
        memb.append(t1)
        
    return names, team, employee, memb


    
#one_to_all - граф, all_persentage - 3 значения (изменился, итоговый и процент чела) 
@router.get("garf/{team_id}/{simple_employee_id}/") 
def get_graf_of_team_and_employee(team_id: int, simple_employee_id: int, db: DbDep):
    one_to_all(get_params_of_team_and_employee(team_id, simple_employee_id, db))
    
    

@router.get("score/{team_id}/{simple_employee_id}/") 
def get_graf_of_team_and_employee(team_id: int, simple_employee_id: int, db: DbDep) -> Tuple[float, float, float]:
    names, team, employee, memb = get_params_of_team_and_employee(team_id, simple_employee_id, db)
    
    return all_percentage(team, memb)



def get_params_random_team(data: List[int], db: DbDep) -> Tuple[float, float]:
    list1 = []
    list1.append(crud_others.get_simple_employee_by_id(db, data[0]))
    for i in range(1, len(data)):
        list1.append(crud_others.get_company_employee_by_id(db, data[i]))
    
    names = {}
    team = []
    
    for i in range(len(list1)):
        for j in range(i, len(list1)):
            names[list1[i].id] = list1[j].name
            s = get_score(convert_bd_data(list1[i].birth_date, list1[i].birth_time), convert_bd_data(list1[j].birth_date, list1[j].birth_time))
            t = tuple[list1[i].id, list1[j].id, s]
            team.append(t)
            
    return names, team



#team_select - все разом (граф, общий процент), принимает словарь ид, имя, список кортежей (ид1б ид2б скор)
@router.get("/company_employees") 
def get_graf_and_score_random_team(data: List[int], db: DbDep) -> Tuple[float, float]:
    names, team = get_params_random_team(data, db)
            
    return team_select(names, team)
    
    
