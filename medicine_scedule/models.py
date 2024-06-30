from sqlalchemy import  Column,String,Date,Integer
from typing import List
from sqlalchemy.orm import relationship
from database import Base
from doctor.models import DoctorViewMedicineSchedule
from patient.models import PatientViewMedicineSchedule
from pharmacist.models import PharmacistAddMedicineSchedule

 
class MedicineSchedule(Base):
    __tablename__ = "medicine_schedules"
        
    ID = Column(Integer, primary_key=True, nullable=False)
    medicine_name = Column(String, nullable=False)
    dose = Column(String, nullable=False)
    doctors = relationship("Doctor",secondary=DoctorViewMedicineSchedule,back_populates="medicine_schedule_views")
    patients = relationship("Patient",secondary=PatientViewMedicineSchedule)
    pharmacists = relationship("Pharmacist",secondary=PharmacistAddMedicineSchedule)   
