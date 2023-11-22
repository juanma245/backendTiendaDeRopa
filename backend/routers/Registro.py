from fastapi import APIRouter
from passlib.context import CryptContext
from esquemas.Usuario import usuarioDB
from conexion.conexion import connection
from constantes.constantes import const


router = APIRouter()
 
@router.post("/registrar",status_code=201)
async def login(usuario : usuarioDB):
    datos = (usuario.usuario, 
             const.crypt.encrypt(usuario.contrasenia),
             usuario.nombre,
             usuario.correo,
             usuario.sexo)
    sql = "INSERT INTO public.usuarios(usuario, contrasenia, nombre, correo, sexo) VALUES (%s, %s, %s, %s, %s);"
    try:
        cursor = connection.cursor()
        cursor.execute(sql,datos)
        connection.commit()
        cursor.close()
        return "Usuario agregado"
    except Exception as ex:
        return ex
   