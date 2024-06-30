from sqlalchemy import  Column,String,Date
from sqlalchemy.orm import relationship
from database import Base
from radiologist.models import RadiologistXrayAdd

    

class Xray(Base):
    __tablename__ = "xrays"
    serial = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False )
    date = Column(Date, nullable=False)
    radiologists = relationship("Xray",secondary=RadiologistXrayAdd)