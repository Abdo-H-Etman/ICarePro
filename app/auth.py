from fastapi import Depends,APIRouter,HTTPException,Response,status
from fastapi.security.oauth2 import OAuth2PasswordRequestForm #{username , password}
from sqlalchemy.orm import Session
# from .. import database,schemas,utils,models,oauth2
from . import schemas,models,oauth2
import utils,database

router = APIRouter(tags= ['Authentication'])

@router.post("/login",response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="wrong email or pasword")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="wrong email or pasword")
    
    #create token
    #retun token
    access_token = oauth2.create_access_token(data= {"user_id": user.ID})
    return {"access_token": access_token,"token_type": "bearer"}