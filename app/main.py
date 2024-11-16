from fastapi import FastAPI

import app.schemas.base
import app.models.create
from app.routes import profile, auth, astro
from app.tmp import migration



app = FastAPI()
res = migration.start()
print(res)

app.include_router(profile.router)
app.include_router(auth.router)
app.include_router(astro.router)