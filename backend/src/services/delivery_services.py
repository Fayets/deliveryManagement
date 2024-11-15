from pony.orm import db_session, desc, select
from fastapi import HTTPException, Query
from typing import Optional
from pony.orm.core import TransactionIntegrityError
from src import models, schemas


class DeliveryServices:
    def __init__(self):
        pass 

    def create_delivery(self, delivery_data: schemas.DeliveryCreate) -> dict:
        with db_session: 
            try:
                # Crear el delivery
                delivery = models.Delivery(
                    nombre = delivery_data.nombre, 
                    apellido = delivery_data.apellido, 
                    dni = delivery_data.dni, 
                    celular = delivery_data.celular,
                )
                print("Usuario creado correctamente.")
                delivery_dict = delivery.to_dict(exclude=['id'])
                return delivery_dict
            except TransactionIntegrityError as e:
                print(f"Error de integridad transaccional: {e}")
                raise HTTPException(
                    status_code=400, detail="Error de integridad al crear el usuario.")
            except Exception as e:
                print(f"Error al crear el usuario: {e}")
                raise HTTPException(
                    status_code=500, detail="Error al crear el usuario.")

        
