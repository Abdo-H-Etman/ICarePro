from app import schemas
from typing import List
from pydantic import BaseModel
import medicine_scedule
import medicine_scedule.models
# import medicine_scedule.schemas
# import medicine_scedule.schemas


class ViewmedicineSchedule(BaseModel):
    doctor_id: int
    medicine_schedule_id: int

class DoctorSignUp(schemas.UserBase):
    specialization: str
    # medicine_schedule_views:List[int]
    pass

class DoctorLogin(schemas.UserLogin):
    pass 


class Doctor(BaseModel):
    user: schemas.UserBase
    specialization: str
    # medicine_schedule_views:List[medicine_scedule.schemas.MedSchedule]
    class Config:
        from_attributes= True   

