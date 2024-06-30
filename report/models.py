from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from database import Base

class Report(Base):
    __tablename__ = "reports"
    serial = Column(String, primary_key=True, nullable=False)
    date = Column(Date, nullable=False ) 
    doctor_id = Column(Integer,
                       ForeignKey("doctors.user_id",ondelete="CASCADE"),
                       nullable=False)  
    patient_id = Column(Integer,
                       ForeignKey("patients.user_id",ondelete="CASCADE"),
                       nullable=False)