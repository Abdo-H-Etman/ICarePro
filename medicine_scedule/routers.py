from database import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,status,Depends,HTTPException

import doctor.routers
from . import models,schemas
import doctor.models
import patient.models
import pharmacist.models

router = APIRouter(
    prefix="/medschedules",
    tags=['medschedules']
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.MedSchedule)
def create_new_schedule(schedule:schemas.MedScheduleCreate,db:Session = Depends(get_db)):
    new_schedule = models.MedicineSchedule(**{k: v for k, v in schedule.model_dump().items() if k not in["doctors","patients","pharmacists"]})
    for doctor_id in schedule.doctors:
        id = db.query(doctor.models.Doctor).get(doctor_id)
        new_schedule.doctors.append(id)

    for patient_id in schedule.patients:
        id = db.query(patient.models.Patient).get(patient_id)
        new_schedule.patients.append(id)

    for pharmacist_id in schedule.pharmacists:
        id = db.query(pharmacist.models.Pharmacist).get(pharmacist_id)
        new_schedule.pharmacists.append(id)

    db.add(new_schedule)
    db.commit()
    db.refresh(new_schedule)    

    return new_schedule

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.MedSchedule)
def get_medschedule(id: int,db: Session = Depends(get_db) ):
    medschedule = db.query(models.MedicineSchedule).filter(models.MedicineSchedule.ID == id).first()
    if not medschedule :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"medicine schedule with id: {id} was not found")
    return medschedule