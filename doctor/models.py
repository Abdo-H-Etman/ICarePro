from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from sqlalchemy.orm import relationship
from database import Base
from app import models
DoctorXrayRequest = Table(
        "doctors_xray_requests",
        Base.metadata,
        Column(
            'doctor_id',
            Integer,
            ForeignKey("doctors.user_id", ondelete="CASCADE"),
            primary_key=True,
            nullable=False,
        ),
        Column(
            'xray_serial',
            String,
            ForeignKey("xrays.serial", ondelete="CASCADE"),
            primary_key=True,
            nullable=False,
        )
)

DoctorXrayView = Table(
    "doctors_xray_views",
    Base.metadata,
    Column(
        'doctor_id',
        Integer,
        ForeignKey("doctors.user_id", ondelete="CASCADE"),
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

DoctorViewMedicineSchedule = Table(
    "doctor_medicine_schedule_views",
    Base.metadata,
    Column(
        'doctor_id',
        Integer,
        ForeignKey("doctors.user_id", ondelete="CASCADE"),
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

class Doctor(Base):
    __tablename__ = "doctors"
    # ID = Column(Integer, primary_key=True, nullable=False)
    # nationalID = Column(String(14), nullable=False)
    # name = Column(String, nullable=False )
    # phone = Column(String, nullable=False, unique=True)
    # date_of_birth = Column(Date, nullable=False)
    # address = Column(String, nullable=False)
    # email = Column(String, nullable=False, unique=True )
    # password = Column(String, nullable=False)
    # gender = Column(String, nullable=False)
    # type = Column(String, nullable=False)
    user_id = Column(Integer,ForeignKey("users.ID",ondelete="CASCADE"),unique= True,primary_key=True)
    user = relationship("User",uselist= False)
    specialization = Column(String, nullable=False )
    xray_requests = relationship("Xray", secondary=DoctorXrayRequest)
    xray_views = relationship("Xray", secondary=DoctorXrayView)
    medicine_schedule_views = relationship("MedicineSchedule", secondary=DoctorViewMedicineSchedule,back_populates="doctors")