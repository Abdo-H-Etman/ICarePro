from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response, APIRouter 
from . import models,schemas
import utils,app.models 

router = APIRouter(
    prefix="/radiologists",
    tags=['radiologists']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Radiologist)
def doctor_sign_up(radiologist:schemas.RadiologistSignUp,db :Session =Depends(get_db)):
    hashed_pass = utils.hash(radiologist.password)
    radiologist.password = hashed_pass
    new_user = app.models.User(**{k: v for k, v in radiologist.model_dump().items() if k != 'center'})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
        
    new_radiologist = models.Radiologist(center=radiologist.model_dump().get("center"),user_id= new_user.ID)
    db.add(new_radiologist)
    db.commit()
    db.refresh(new_radiologist)

    return {'user':new_user,'center':new_radiologist.center}

@router.get("/{id}",response_model=schemas.Radiologist)
def get_labphysician_profile(id:int, db: Session = Depends(get_db)):
    radiologist = db.query(app.models.User).filter(app.models.User.ID == id).first()
    center = db.query(models.Radiologist).filter(models.Radiologist.user_id == id).first().center
    if not radiologist :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"doctor with id: {id} was not found")
    return {'user':radiologist,'center':center}