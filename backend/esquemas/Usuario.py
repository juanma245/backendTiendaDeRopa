from pydantic import BaseModel

class datosLogin(BaseModel):
    usuario : str
    contrasenia : str

class usuario(BaseModel):
    idUsuario : int | None = None
    usuario : str
    nombre : str
    correo : str
    sexo : str

class usuarioDB(usuario):
    contrasenia : str

