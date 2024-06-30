from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response, APIRouter 
from . import models,schemas
import utils,app.models

router = APIRouter(
    prefix="/pharmacists",
    tags=['pharmacists']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Pharmacist)
def doctor_sign_up(pharmacist:schemas.PharmacistSignUp,db :Session =Depends(get_db)):
    hashed_pass = utils.hash(pharmacist.password)
    pharmacist.password = hashed_pass
    new_user = app.models.User(**{k: v for k, v in pharmacist.model_dump().items()})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
        
    new_pharmacist = models.Pharmacist(user_id = new_user.ID)
    db.add(new_pharmacist)
    db.commit()
    db.refresh(new_pharmacist)

    return {'user': new_user}

@router.get("/{id}",response_model=schemas.Pharmacist)
def get_labphysician_profile(id:int, db: Session = Depends(get_db)):
    pharmacist = db.query(app.models.User).filter(app.models.User.ID == id).first()
    if not pharmacist :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"doctor with id: {id} was not found")
    return {'user':pharmacist}