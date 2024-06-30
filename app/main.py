from fastapi import FastAPI
import psycopg
import time
import doctor.routers
import labphysician.routers
#import medicine_scedule,doctor,labphysician,patient,pharmacist,radiologist
from database import engine
from sqlalchemy.orm import Session
from psycopg.rows import dict_row
from config import Base
import medicine_scedule.routers
import patient.routers
import pharmacist.routers
import radiologist.routers
from . import auth


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg.connect(host='localhost',dbname='test',user='postgres',password='fastapiapp'     
                               ,row_factory=dict_row)
        cursor = conn.cursor()
        print("database connection was succesful") 
        break
    except Exception as exc: 
        print("connection failed") 
        print(exc)
        time.sleep(2)     


app = FastAPI()

app.include_router(doctor.routers.router)
app.include_router(medicine_scedule.routers.router)
app.include_router(labphysician.routers.router)
app.include_router(patient.routers.router)
app.include_router(pharmacist.routers.router)
app.include_router(radiologist.routers.router)
app.include_router(auth.router)