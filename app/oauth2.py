from jose import JWTError,jwt
from datetime import datetime,timedelta, timezone
from fastapi import status,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer
from . import schemas,models
import database
from sqlalchemy.orm import Session

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')
def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt 

def verify_access_token(token: str, credentials_exeption):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        if id is None:
            raise credentials_exeption
        token_data = schemas.tokenData(id= id)
    except JWTError:
        raise credentials_exeption

    return token_data

def get_current_user(token: str = Depends(oauth2_schema),db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"wrong user name or password ",
                                          headers={"WWW-Authenticate":"bearer"}) 
    
    token = verify_access_token(token,credentials_exception)
    user  = db.query(models.User).filter(models.User.ID == token.id).first()
    return   user