from pony.orm import * 
from src.db import db
from enum import Enum
from datetime import date, datetime


class Roles(str, Enum):
    ADMIN = "ADMIN"

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(str)
    role = Required(str)

    _table_ = "Usuario"

class Delivery(db.Entity):
    id = PrimaryKey(int, auto=True)
    nombre = Required(str) 
    apellido = Required(str)  
    dni = Required(str)  
    celular = Required(str) 
    pedido = Set('Pedido')

    _table_ = "Delivery"

class Pedido(db.Entity): 
    id = PrimaryKey(int, auto=True)
    direccion_entrega = Required(str)
    productos = Required(str) # Lista de productos del pedido
    precio_delivery = Required(float) # Costo del servicio de delivery
    precio_total = Required(float)  # Precio total del pedido
    fecha_pedido = Required(datetime, default=datetime.now)
    estado = Required(str, default='Pendiente') # Estado del pedido: 'Pendiente', 'En camino', 'Entregado', 'Pagado'
    delivery = Optional(Delivery)

    _table_ = "Pedido"
    