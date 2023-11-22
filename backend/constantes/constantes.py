from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from jose import jwt,JWTError


class const():
    ALGORITHM = "HS256"
    ACCESS_DURATION = 60
    crypt = CryptContext(schemes=["bcrypt"])
    SECRET = "7acdfa8ad391517ccf8ccff80a19674dS"
    oauth2 = OAuth2PasswordBearer(tokenUrl="login/")

    
async def authId(token : str = Depends(const.oauth2)):
    try:
        id = jwt.decode(token, const.SECRET, algorithms=[const.ALGORITHM]).get("sub")
        if id is None:
            print("mirame")
            return None
    except JWTError as ex:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=ex)
    
    return id