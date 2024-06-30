import app.models
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response, APIRouter 
from . import models,schemas
import utils,app

router = APIRouter(
    prefix="/patients",
    tags=['patients']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Patient)
def doctor_sign_up(patient:schemas.PatientSignUp,db :Session =Depends(get_db)):
    hashed_pass = utils.hash(patient.password)
    patient.password = hashed_pass
    new_user = app.models.User(**{k: v for k, v in patient.model_dump().items()})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    new_patient = models.Patient(user_id= new_user.ID)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return {'user':new_user}

@router.get("/{id}",response_model=schemas.Patient)
def get_labphysician_profile(id:int, db: Session = Depends(get_db)):
    patient = db.query(app.models.User).filter(app.models.User.ID == id).first()
    if not patient :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"doctor with id: {id} was not found")
    return { 'user': patient}