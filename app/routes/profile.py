from fastapi import APIRouter, Depends, HTTPException, UploadFile
import app.utils
from app.schemas.user import User, UserUpdate, ProfileRegister
from app.schemas.others import AdvertRead, ResponseRead, AdvertCreate
import app.crud.user as crud_user
import app.crud.others as crud_others

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/all")
def get_all(db: app.utils.DbDep) -> list[User]:
    return crud_user.get_all_users(db)

@router.post("/new/")
def create_profile(data: ProfileRegister, db: app.utils.DbDep) -> User:
    user = crud_user.create_user(db, **data.model_dump())
    return user


@router.get("/{id}/")
def get_profile(id: int, db: app.utils.DbDep) -> User:
    user = crud_user.get_user_by_id(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user



@router.get("/{id}/adverts/")
def get_adverts(id: int, db: app.utils.DbDep) -> list[AdvertRead]:
    adverts = crud_user.get_user_adverts(db, id)
    if not adverts:
        raise HTTPException(status_code=404, detail="Adverts not found")
    return adverts


@router.post("/{id}/add_advert")
def post_advert(db: app.utils.DbDep, data: AdvertCreate) -> AdvertRead:
    advert = crud_others.create_company_advert(db, **data.model_dump())
    return advert


@router.get("/{id}/adverts/{advert_id}")
def get_advert_by_id(id: int, advert_id: int, db: app.utils.DbDep) -> AdvertRead:
    adverts = crud_user.get_user_adverts(db, id)
    if not adverts:
        raise HTTPException(status_code=404, detail="Adverts not found")
    
    for advert in adverts:
        if advert.id == advert_id:
            return advert
        
    raise HTTPException(status_code=404, detail="Advert not found")

# @router.get("/{id}/adverts/{advert_id}/responses")
    

@router.get("/{id}/responses")
def get_all_user_responses(id: int, db: app.utils.DbDep) -> list[ResponseRead]:
    responses = crud_user.get_user_responses(db, id)
    
    if not responses:
        raise HTTPException(status_code=404, detail="Response not found")
    
    return responses


@router.get("/{id}/responses/{response_id}")
def get_response_by_id(id: int, response_id: int, db: app.utils.DbDep) -> ResponseRead:
    response = crud_others.get_response_by_id(db, response_id)
    
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
