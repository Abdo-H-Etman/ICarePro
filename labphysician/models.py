from sqlalchemy import  Column,String,Date,Integer,ForeignKey,Table,Double
from sqlalchemy.orm import relationship
from database import Base


LabPhysicianAnalysisAdd = Table(
    "lab_physician_analysis_adds",
    Base.metadata,            
    Column(
        'lab_physician_id',
        Integer,
        ForeignKey("labphysicians.user_id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
        ),
    Column(
        'analysis_serial',
        String,
        ForeignKey("analyses.serial", ondelete="CASCADE"),
        primary_key=True,
        nullable=False
        )
)


class LabPhysician(Base):
    __tablename__ = "labphysicians"
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
    lab_name = Column(String, nullable=False)
    analysis_added = relationship("Analysis",secondary=LabPhysicianAnalysisAdd)