from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from sqlalchemy.orm import relationship
from database import Base

PatientXrayView = Table(
    "patients_xray_views",
    Base.metadata,
    Column(
        'patient_id',
        Integer,
        ForeignKey("patients.user_id", ondelete="CASCADE"),
        primary_key=True, 
        nullable=False
        ),          
    Column(
        'xray_serial',
        String,
        ForeignKey("xrays.serial", ondelete="CASCADE"),
        primary_key=True, 
        nullable=False
        ) 
)

PatientViewMedicineSchedule = Table(
    "patient_medicine_schedule_views",
    Base.metadata,
    Column(
        'patient_id',
        Integer,
        ForeignKey("patients.user_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    ),     
    Column(
        'medicine_schedule_id',
        Integer,
        ForeignKey("medicine_schedules.ID", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
    )   
)

class Patient(Base):
    __tablename__ = "patients"
    
    user_id = Column(Integer,ForeignKey("users.ID",ondelete="CASCADE"),unique= True,primary_key=True)
    user = relationship("User",uselist= False)
    xray_views = relationship("Xray",secondary=PatientXrayView)
    medicine_scheduel_views = relationship("MedicineSchedule",secondary=PatientViewMedicineSchedule)

class InsulinLevel(Base):
    __tablename__ = "insulinlevels"  
    ID = Column(Integer,primary_key=True,nullable=False) 
    date = Column(Date, nullable=False )
    type = Column(String, nullable=False)
    result = Column(Integer, nullable=False)
    patient_id = Column(
        Integer,
        ForeignKey("patients.user_id", ondelete="CASCADE"),
        nullable=False)   

class BloodPressure(Base):
    __tablename__ = "blood_pressures"
    ID = Column(Integer,primary_key=True,nullable=False) 
    systolic = Column(Double,nullable=False)
    diastolic = Column(Double,nullable=False)
    pulse = Column(Double,nullable=False)
    patient_id = Column(
        Integer,
        ForeignKey("patients.user_id", ondelete="CASCADE"),
        nullable=False)
    
