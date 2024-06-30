from app import schemas
from pydantic import BaseModel
class RadiologistSignUp(schemas.UserBase):
    center: str
    pass

class RadiologistLogin(schemas.UserLogin):
    pass 

class Radiologist(BaseModel):
    user:schemas.UserBase
    center: str
    class Config:
        from_attributes= True