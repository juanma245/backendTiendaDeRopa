from fastapi import APIRouter,Depends,HTTPException,status
from esquemas.Producto import Producto
from conexion.conexion import connection
from constantes.constantes import authId

router = APIRouter()
  
@router.post("/productos/agregar/",status_code=201)
async def agregarProducto(producto: Producto, id : str = Depends(authId)):

    if id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="no autorizado")

    datos = (producto.idTienda,producto.nombre, producto.precio,producto.imagen,producto.tipo,producto.talla)
    sql = "INSERT INTO public.productos(idtienda, nombre, precio, imagen, tipo, talla) VALUES (%s, %s, %s, %s, %s, %s)"
    
    try:
        
        cursor = connection.cursor()
        cursor.execute(sql,datos)
        connection.commit()
        cursor.close()
        return "se agrego correctamente"
    except Exception as ex:
        return ex
    
    