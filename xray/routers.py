from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,status,Depends,HTTPException
from . import models,schemas
import radiologist.models

router = APIRouter(
    prefix="/xrays",
    tags=['xrays']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Xray)
def create_new_report(xray:schemas.XrayCreate,db:Session = Depends(get_db)):
    new_xray = models.Xray(**{k: v for k, v in xray.model_dump().items() if k != "radiologists"})
    
    for radiologist_id in xray.radiologists:
        id = db.query(radiologist.models.Radiologist).get(radiologist_id)
        new_xray.radiologists.append(id)

    db.add(new_xray)
    db.commit()
    db.refresh(new_xray)

    return new_xray

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.Xray)
def get_medschedule(id: str,db: Session = Depends(get_db) ):
    xray = db.query(models.Xray).filter(models.Xray.serial == id).first()
    if not xray :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"xray with serial: {id} was not found")
    return xray