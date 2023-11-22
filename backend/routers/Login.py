from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt
from datetime import datetime, timedelta
from conexion.conexion import connection
from constantes.constantes import const


router = APIRouter()


def buscarUsuario(usuario : str):
    sql = "SELECT idusuario, contrasenia FROM public.usuarios where usuario = %s ;"    
    try:
        cursor = connection.cursor()
        cursor.execute(sql,(usuario,))
        registro = cursor.fetchone()
        connection.commit()
        cursor.close()
        if registro is None:
           return None
        return registro
    except Exception as ex:
        print("joder")
        return ex


@router.post("/login/")
async def login(form : OAuth2PasswordRequestForm = Depends()):
    username = form.username
    
    usuario = buscarUsuario(username)
    if usuario is None:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail= "Usuario incorrecto")
    if not const.crypt.verify(form.password, usuario[1]):
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail= "Contraseña incorrecta")

    token = {"sub" : str(usuario[0]),
             "exp": datetime.utcnow() + timedelta(minutes=const.ACCESS_DURATION)}
    
    
    return{"access_token" : jwt.encode(token,const.SECRET,algorithm=const.ALGORITHM), "toke_type" : "bearer"}
