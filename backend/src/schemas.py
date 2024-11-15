from pydantic import BaseModel
from typing import List, Optional
from src.models import Roles
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class RegisterMessage(BaseModel):
    message: str
    success: bool

class LoginRequest(BaseModel):
    username: str | None = None
    password: str | None = None

class DeliveryCreate(BaseModel):
    nombre: str 
    apellido: str 
    celular: str 
    dni: str

class PedidoCreate(BaseModel):
    productos: str
    direccion_entrega: str
    precio_delivery: float  # Cambié el tipo a float para que coincida con el modelo
    precio_total: float
    fecha_pedido: Optional[datetime] = None
    estado: str  # Estado del pedido ('Pendiente', 'En camino', 'Entregado', 'Pagado')
    dni_delivery: str  # DNI del delivery asignado al pedido

    class Config:
        orm_mode = True  # Permite que el modelo trabaje con la base de datos


