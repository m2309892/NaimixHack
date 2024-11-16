from app.models.create import LocalSession
from typing import Annotated, TYPE_CHECKING
from fastapi import Depends

from sqlalchemy.orm import Session

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

DbDep = Annotated[Session, Depends(get_db)]