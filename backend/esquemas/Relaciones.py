from pydantic import BaseModel

class productoPertenece(BaseModel):
    idCatalogo : int
    idProducto : int