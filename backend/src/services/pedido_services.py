from pony.orm import db_session
from fastapi import HTTPException, status
from pony.orm.core import TransactionIntegrityError
from src import models, schemas
from datetime import datetime


class PedidoServices:
    def __init__(self):
        pass 

    @db_session  # Asegura que la transacción se maneje correctamente
    def create_pedido(self, pedido_data: schemas.PedidoCreate):
        try:
            # Buscar el delivery por DNI
            delivery = models.Delivery.get(dni=pedido_data.dni_delivery)
            
            # Si no se encuentra el delivery, lanzar un error
            if not delivery:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Delivery con DNI {pedido_data.dni_delivery} no encontrado."
                )

            # Crear el pedido
            pedido = models.Pedido(
                productos=pedido_data.productos,
                direccion_entrega=pedido_data.direccion_entrega,
                precio_delivery=pedido_data.precio_delivery,
                precio_total=pedido_data.precio_total,
                fecha_pedido=pedido_data.fecha_pedido or datetime.now(),  # Usa la fecha actual si no se especifica
                estado=pedido_data.estado,
                delivery=delivery  # Asigna el delivery al pedido usando el DNI
            )

            # Commit de los cambios (los cambios se guardan automáticamente con db_session)
            print("Pedido creado correctamente.")
            
            # Opcional: Convertir el pedido a un diccionario para retornarlo
            pedido_dict = pedido.to_dict(exclude=['id'])
            
            return pedido_dict
        
        except TransactionIntegrityError as e:
            print(f"Error de integridad transaccional: {e}")
            raise HTTPException(
                status_code=400, detail="Error de integridad al crear el pedido."
            )
        except Exception as e:
            print(f"Error al crear el pedido: {e}")
            raise HTTPException(
                status_code=500, detail="Error al crear el pedido."
            )
