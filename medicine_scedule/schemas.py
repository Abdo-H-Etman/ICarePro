from pydantic import BaseModel
from typing import List
# from doctor import schemas
import doctor.schemas
import patient.schemas
import pharmacist.schemas

class MedScheduleBase(BaseModel):
    medicine_name: str
    dose: str

class MedScheduleCreate(MedScheduleBase):
    doctors:List[int]
    patients:List[int]
    pharmacists:List[int]
    

class MedSchedule(MedScheduleBase):
    ID: int
    doctors:List[doctor.schemas.Doctor]
    patients:List[patient.schemas.Patient]
    pharmacists:List[pharmacist.schemas.Pharmacist]
    class Config:
        from_attributes= True