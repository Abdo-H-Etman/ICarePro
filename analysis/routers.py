from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,status,Depends,HTTPException
from . import models,schemas

router = APIRouter(
    prefix="/analysis",
    tags=['analysis']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Analysis)
def create_new_report(analysis:schemas.AnalysisCreate,db:Session = Depends(get_db)):
    new_analysis = models.Analysis(**analysis.model_dump())
    db.add(new_analysis)
    db.commit()
    db.refresh(new_analysis)

    return new_analysis

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Analysis)
def get_medschedule(id: str,db: Session = Depends(get_db) ):
    analysis = db.query(models.Analysis).filter(models.Analysis.serial == id).first()
    if not analysis :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"analysis with serial: {id} was not found")
    return analysis