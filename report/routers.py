from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,status,Depends,HTTPException
from . import models,schemas

router = APIRouter(
    prefix="/reports",
    tags=['reports']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Report)
def create_new_report(schedule:schemas.ReportCreate,db:Session = Depends(get_db)):
    new_report = models.Report(**schedule.model_dump())
    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    return new_report

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Report)
def get_medschedule(id: str,db: Session = Depends(get_db) ):
    report = db.query(models.Report).filter(models.Report.serial == id).first()
    if not report :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"report with serial: {id} was not found")
    return report