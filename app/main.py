from fastapi import FastAPI

import app.schemas.base
import app.models.create
from app.routes import profile, auth, astro



app = FastAPI()

app.include_router(profile.router)
app.include_router(auth.router)
app.include_router(astro.router)