from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from sqlalchemy.orm import relationship
from database import Base

RadiologistXrayAdd = Table(
    "radiologists_xray_adds",
    Base.metadata,
    Column(
        'radiologist_id',
        Integer,
        ForeignKey("radiologists.user_id", ondelete="CASCADE"),
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

class Radiologist(Base):
    __tablename__ = "radiologists"
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
    center = Column(String, nullable=False)
    xrays_added = relationship("Xray",secondary=RadiologistXrayAdd)