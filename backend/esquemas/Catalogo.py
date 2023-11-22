from pydantic import BaseModel

class Catalogo(BaseModel):
    idCatalogo : int | None = None
    idTienda : int
    nombre : str
    exhibido : bool = False