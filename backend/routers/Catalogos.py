from fastapi import APIRouter,Depends,HTTPException,status
from esquemas.Catalogo import Catalogo
from esquemas.Relaciones import productoPertenece
from conexion.conexion import connection
from constantes.constantes import authId

router = APIRouter()


@router.post("/catalogos/Crear/", status_code=201)
async def crearCatalogo(catalogo : Catalogo,id : str = Depends(authId)):
    
    if id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="no autorizado")
    
    datos = (catalogo.idTienda,catalogo.nombre,catalogo.exhibido)
    sql = "INSERT INTO public.catalogos(idtienda, nombre, exibhido) VALUES (%s, %s, %s);"

    try:
        cursor = connection.cursor()
        cursor.execute(sql,datos)
        connection.commit()
        cursor.close()
        return "catalogo creado"
    except Exception as ex:
        return ex
    
@router.put("/catalogos/publicar/")
async def publicarCatalogo(catalogo : Catalogo, id : str = Depends(authId)):
    if id is None:
       raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="no autorizado")
    
    datos = (catalogo.exhibido, catalogo.idTienda, catalogo.nombre )
    sql = "UPDATE public.catalogos SET exibhido=%s WHERE idtienda = %s and nombre = %s;"

    try:
        cursor = connection.cursor()
        cursor.execute(sql,datos)
        connection.commit()
        cursor.close()
        return "catalogo modificado"
    except Exception as ex:
        return ex
    
@router.post("/catalogos/modificar/")
async def modificarCatalogo(p : productoPertenece, id : str = Depends(authId)):
    if id is None:
        return "no autorizado"

    datos = (p.idCatalogo,p.idProducto)
    sql = 'INSERT INTO public."perteneceAcatalogo"(idcatalogo, idproducto) VALUES (%s, %s);'

    try:
        cursor = connection.cursor()
        cursor.execute(sql,datos)
        connection.commit()
        cursor.close()
        return "producto agregado"
    except Exception as ex:
        return ex

    