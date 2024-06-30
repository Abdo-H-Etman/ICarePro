from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    ID = Column(Integer, primary_key=True, nullable=False)
    nationalID = Column(String(14), nullable=False)
    name = Column(String, nullable=False )
    phone = Column(String, nullable=False, unique=True)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True )
    password = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    type = Column(String, nullable=False)