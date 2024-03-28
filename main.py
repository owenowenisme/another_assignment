from fastapi import FastAPI
from routers import routers
from model import model
from db.db import engine
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.router)
