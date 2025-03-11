from pydantic import BaseModel

class VetBase(BaseModel):
    name: str
    phone: str
    email: str
    address: str
    image_uri: str

class VetCreate(VetBase):
    pass

class Vet(VetBase):
    id: int

    class Config:
        orm_mode = True