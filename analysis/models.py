from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from database import Base

class Analysis(Base):
    __tablename__ = "analyses"
    serial = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False )
    date = Column(Date, nullable=False) 