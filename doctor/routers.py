from typing import List
import app.models
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Response, APIRouter
import app.schemas

import medicine_scedule.models as medimodels
import medicine_scedule.models
from . import models,schemas
import medicine_scedule
import utils

router = APIRouter(
    prefix="/doctors",
    tags=['doctors']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Doctor)
def doctor_sign_up(doctor: schemas.DoctorSignUp,db :Session =Depends(get_db)):
    hashed_pass = utils.hash(doctor.password)
    doctor.password = hashed_pass
    new_user = app.models.User(**{k: v for k, v in doctor.model_dump().items() if k not in["specialization","medicine_schedule_views"]})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    new_doctor = models.Doctor(specialization=doctor.model_dump().get("specialization"),user_id= new_user.ID)

    # for schedule_id in doctor.medicine_schedule_views:
    #     schedule = db.query(medicine_scedule.models.MedicineSchedule).get(schedule_id)
    #     new_doctor.medicine_schedule_views.append(schedule)

    db.add(new_doctor)
    db.commit()
    db.refresh(new_doctor)

    
    return {'user':new_user,'specialization':new_doctor.specialization}

@router.get("/{id}",response_model=schemas.Doctor)
def get_doctor_profile(id:int, db: Session = Depends(get_db)):
    doctor = db.query(app.models.User).filter(app.models.User.ID == id).first()
    specialization = db.query(models.Doctor).filter(models.Doctor.user_id == id).first().specialization 
    views = db.query(models.Doctor).filter( models.Doctor.user_id == id).first().medicine_schedule_views
    if not doctor :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"doctor with id: {id} was not found")
    return {'user': doctor, 'specialization': specialization,'medicine_schedule_views':views}

@router.post("/views",response_model=schemas.ViewmedicineSchedule)
def new_view(view:schemas.ViewmedicineSchedule,db:Session = Depends(get_db)):
    new_view = models.DoctorViewMedicineSchedule(**view.model_dump())
    db.add(new_view)
    db.commit()
    db.refresh(new_view)

    return new_view