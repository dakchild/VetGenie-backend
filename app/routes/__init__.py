from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import Vet, VetCreate
from app.services import get_vets, create_vet
from app.models import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/vets/", response_model=list[Vet])
def read_vets(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    vets = get_vets(db, skip=skip, limit=limit)
    return vets

@router.post("/vets/", response_model=Vet)
def create_vet(vet: VetCreate, db: Session = Depends(get_db)):
    return create_vet(db=db, vet=vet)