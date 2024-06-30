from pydantic import BaseModel
from typing import List
from datetime import date
import  radiologist.schemas
class XrayBase(BaseModel):
    name:str
    date: date

class XrayCreate(XrayBase):
    radiologists:List[int]
    pass

class Xray(XrayBase):
    serial: str
    radiologists:List[radiologist.schemas.Radiologist]
    class Config:
        from_attributes= True