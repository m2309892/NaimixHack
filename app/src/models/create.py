from app.src.models.base import Base
from sqlalchemy import create_engine
from app.src.models.config import config

url = f'postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:{config.POSTGRES_PORT}/{config.POSTGRES_DB}'
engine = create_engine(
    url,
    future=True,
    echo=False,
    pool_pre_ping=True
)

if config.reset_db:
    Base.metadata.drop_all(engine)

Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
LocalSession = sessionmaker(bind=engine)
