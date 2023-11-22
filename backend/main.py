from fastapi import FastAPI
from routers import Registro,Productos,Catalogos,Login

#iniciar server
#uvicorn main:app --reload
#server http://127.0.0.1:8000


app = FastAPI()

app.include_router(Registro.router)
app.include_router(Productos.router)
app.include_router(Catalogos.router)
app.include_router(Login.router)



@app.get("/iniciar")
async def root():
    return "prueba"
