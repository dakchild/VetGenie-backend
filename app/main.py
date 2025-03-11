from fastapi import FastAPI
from app.routes import router as vet_router
from app.models import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vet_router, prefix="/api")