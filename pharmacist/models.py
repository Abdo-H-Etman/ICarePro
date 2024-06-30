from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from sqlalchemy.orm import relationship
from database import Base

PharmacistAddMedicineSchedule = Table(
    "pharmacist_medicine_schedule_adds",
    Base.metadata,
    Column(
        'pharmacist_id',
        Integer,
        ForeignKey("pharmacists.user_id"),
        primary_key=True,
        nullable=False
    ),     
    Column(
        'medicine_schedule_id',
        Integer,
        ForeignKey("medicine_schedules.ID"),
        primary_key=True,
        nullable=False
    )    
)

class Pharmacist(Base):
    __tablename__ = "pharmacists"
    # ID = Column(Integer, primary_key=True, nullable=False)
    # nationalID = Column(String, nullable=False)
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
    medicine_schedule_adds = relationship("MedicineSchedule",secondary=PharmacistAddMedicineSchedule)   
