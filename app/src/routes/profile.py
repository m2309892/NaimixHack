from fastapi import APIRouter, Depends, HTTPException, UploadFile
import app.src.utils
from app.src.schemas.user import User, UserUpdate, ProfileRegister
from app.src.schemas.others import AdvertRead, ResponseRead, AdvertCreate, CompanyEmployeeRead, CompanyEmployeeCreate, TeamCreate, TeamRead
import app.src.crud.user as crud_user
import app.src.crud.others as crud_others
from app.src.utils import DbDep

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/all")
def get_all(db: DbDep) -> list[User]:
    return crud_user.get_all_users(db)


@router.post("/new/")
def create_profile(data: ProfileRegister, db: DbDep) -> User:
    user = crud_user.create_user(db, **data.model_dump())
    return user


@router.get("/{id}/")
def get_profile(id: int, db: DbDep) -> User:
    user = crud_user.get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/{id}/adverts/")
def get_adverts(id: int, db: DbDep) -> list[AdvertRead]:
    adverts = crud_user.get_user_adverts(db, id)
    if not adverts:
        raise HTTPException(status_code=404, detail="Adverts not found")
    return adverts


@router.post("/{id}/add_advert")
def post_advert(db: DbDep, data: AdvertCreate) -> AdvertRead:
    advert = crud_others.create_company_advert(db, **data.model_dump())
    return advert


@router.get("/{id}/adverts/{advert_id}")
def get_advert_by_id(id: int, advert_id: int, db: DbDep) -> AdvertRead:
    adverts = crud_user.get_user_adverts(db, id)
    if not adverts:
        raise HTTPException(status_code=404, detail="Adverts not found")
    
    for advert in adverts:
        if advert.id == advert_id:
            return advert
        
    raise HTTPException(status_code=404, detail="Advert not found")

# @router.get("/{id}/adverts/{advert_id}/responses")
    

@router.get("/{id}/responses")
def get_all_user_responses(id: int, db: DbDep) -> list[ResponseRead]:
    responses = crud_user.get_user_responses(db, id)
    
    if not responses:
        raise HTTPException(status_code=404, detail="Response not found")
    
    return responses


@router.get("/{id}/responses/{response_id}")
def get_response_by_id(id: int, response_id: int, db: DbDep) -> ResponseRead:
    response = crud_others.get_response_by_id(db, response_id)
    
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    
    return response


@router.get("/{id}/employees")
def get_company_employees(id: int, db: DbDep) -> list[CompanyEmployeeRead]:
    response = crud_user.get_user_employees(db, id)
    
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    
    return response


@router.post("/{id}/employees/add_employee")
def create_company_employee(db: DbDep, data: CompanyEmployeeCreate) -> CompanyEmployeeRead:
    response = crud_others.create_company_employee(db, **data.model_dump())
    return response


@router.post("/{id}/employees/add_team")
def create_company_team(db: DbDep, data: TeamCreate) -> TeamRead:
    response = crud_others.create_company_team(db, **data.model_dump())
    return response
    

@router.get("/{id}/employees/teams")
def get_company_teams(db: DbDep, id: int) -> list[TeamRead]:
    response = crud_user.get_user_teams(db, id)
    
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    
    return response


@router.get("/{id}/employees/{employee_id}")
def get_company_employee(db: DbDep, employee_id: int, id: int) -> CompanyEmployeeRead:
    response = crud_others.get_company_employee_by_id(db, employee_id)
    
    if not response:
        raise HTTPException(status_code=404, detail="Response not found")
    
    return response


# @router.patch("/{id}/update/")
# def update_profile(id: int, data: UserUpdate, db: app.utils.DbDep) -> User:
#     user = crud_user.update_user(db, id, **data.model_dump(exclude_none=True))
#     if not user:
#         raise HTTPException(status_code=404,
#                             detail="User not found")
#     return user





# @router.post("/{id}/photo/")
# def upload_file(id: int, photo: UploadFile, db: app.utils.DbDep) -> dict:
#     link = crud_user.update_user_photo(db, id, photo.file.read())
#     return {"link": link}
