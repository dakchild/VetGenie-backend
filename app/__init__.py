from sqlalchemy.orm import Session
from app.models import Vet
from app.schemas import VetCreate

def get_vets(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Vet).offset(skip).limit(limit).all()

def create_vet(db: Session, vet: VetCreate):
    db_vet = Vet(**vet.dict())
    db.add(db_vet)
    db.commit()
    db.refresh(db_vet)
    return db_vet