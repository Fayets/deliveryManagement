import uvicorn
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from src.db import db
from src.controllers.auth_controller import router as auth_router
from src.controllers.delivery_controller import router as delivery_router
from src.controllers.pedido_controller import router as pedido_router

app = FastAPI() #creamos una instancia. Este será el punto de interacción principal para crear todo tu API.

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)

# Mapeando las entidades a tablas (si no existe la tabla, la crea)
db.generate_mapping(create_tables=True)

#Lista de Rutas

#Auth 
app.include_router(auth_router, prefix="/auth", tags=["auth"])

#Delivery
app.include_router(delivery_router, prefix="/delivery", tags=["delivery"])

#Pedido
app.include_router(pedido_router, prefix="/pedido", tags=["pedido"])


