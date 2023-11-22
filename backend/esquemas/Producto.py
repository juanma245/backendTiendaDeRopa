from pydantic import BaseModel

class Producto(BaseModel):
    idProducto : int | None = None
    idTienda : int 
    nombre : str
    precio: int
    imagen : str
    tipo: int
    talla: str