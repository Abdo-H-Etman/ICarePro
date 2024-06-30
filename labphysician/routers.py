import app.models
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response, APIRouter 
from . import models,schemas
import utils,app

router = APIRouter(
    prefix="/labphysicians",
    tags=['labphysicians']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.LabPhysician)
def doctor_sign_up(labphysician:schemas.LabPhysicianSignUp,db :Session =Depends(get_db)):
    hashed_pass = utils.hash(labphysician.password)
    labphysician.password = hashed_pass
    new_user = app.models.User(**{k: v for k, v in labphysician.model_dump().items() if k != "lab_name"})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    new_doctor = models.LabPhysician(lab_name=labphysician.model_dump().get("lab_name"),user_id= new_user.ID)
    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    return {'user':new_user,'lab_name':new_doctor.lab_name}

@router.get("/{id}",response_model=schemas.LabPhysician)
def get_labphysician_profile(id:int, db: Session = Depends(get_db)):
    labpysician = db.query(app.models.User).filter(app.models.User.ID == id).first()
    lab_name = db.query(models.LabPhysician).filter(models.LabPhysician.user_id == id).first().lab_name
    if not labpysician :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"doctor with id: {id} was not found")
    return {'user': labpysician, 'lab_name': lab_name}