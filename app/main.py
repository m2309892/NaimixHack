from fastapi import FastAPI

import app.schemas.base
import app.models.create
from app.routes import profile, auth, events



app = FastAPI()

app.include_router(profile.router)
app.include_router(auth.router)