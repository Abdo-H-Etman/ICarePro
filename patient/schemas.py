from app import schemas
from pydantic import BaseModel


class PatientSignUp(schemas.UserBase):
    pass    

class PatientLogin(schemas.UserLogin):
    pass

class Patient(BaseModel):
    user: schemas.UserBase
    class Config:
        from_attributes= True