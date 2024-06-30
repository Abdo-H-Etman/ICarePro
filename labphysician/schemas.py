from app import schemas
from pydantic import BaseModel
class LabPhysicianSignUp(schemas.UserBase):
    lab_name: str
    pass

class LabPhysicianLogin(schemas.UserLogin):
    pass 

class LabPhysician(BaseModel):
    user: schemas.UserBase
    lab_name:str
    class Config:
        from_attributes= True

        