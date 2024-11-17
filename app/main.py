from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import app.src.schemas.base
import app.src.models.create
from app.src.routes import profile, auth, astro
from app.src.tmp import migration



app = FastAPI()
res = migration.start()
print(res)

app.include_router(profile.router)
app.include_router(auth.router)
app.include_router(astro.router)

app.mount("/static", 
  StaticFiles(directory='/root/svg_data'
), 
name="static_files")
