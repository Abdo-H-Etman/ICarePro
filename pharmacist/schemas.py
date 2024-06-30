from app import schemas
from pydantic import BaseModel
class PharmacistSignUp(schemas.UserBase):
    pass

class PharmacistLogin(schemas.UserLogin):
    pass 

class Pharmacist(BaseModel):
    user: schemas.UserBase
    class Config:
        from_attributes= True