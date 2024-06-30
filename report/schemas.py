from pydantic import BaseModel
from datetime import date
class ReportBase(BaseModel):
    date:date
    doctor_id: int
    patient_id: int

class ReportCreate(ReportBase):
    pass

class Report(ReportBase):
    serial: str
    class Config:
        from_attributes= True