from pydantic import BaseModel
from datetime import date
class AnalysisBase(BaseModel):
    name: str
    date: date

class AnalysisCreate(AnalysisBase):
    pass


class Analysis(AnalysisBase):
    serial:str
    class Config:
        from_attributes= True
        

