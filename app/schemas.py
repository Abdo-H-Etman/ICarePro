from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    password: str
    nationalID: str
    gender: str
    phone: str
    address: str
    date_of_birth: date
    type: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    type: str

class userProfile(BaseModel):
    name: str
    email: EmailStr
    nationalID: str
    gender: str
    phone: str
    address: str
    date_of_birth: date
    type: str    

class Token(BaseModel):
    access_token: str
    token_type:str

class tokenData(BaseModel):
    id: Optional[int] = None     