from fastapi import HTTPException, APIRouter,status, Depends
from pony.orm import *
from src import schemas
from src.schemas import RegisterMessage, UserCreate
from jose import jwt, JWTError, ExpiredSignatureError
from src.services.delivery_services import DeliveryServices
from pydantic import BaseModel
from decouple import config
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta

router = APIRouter()

service = DeliveryServices()

@router.post("/register", response_model=RegisterMessage, status_code=201)
def register_delivery(delivery: schemas.DeliveryCreate):
    try:
        delivery_created = service.create_delivery(delivery)
        return {
            "message": "Delivery creado correctamente",
            "success": True,
        }
    except HTTPException as e:
        # Maneja el error y devuelve un mensaje personalizado
        return {
            "message": e.detail,
            "success": False,
        }
    except Exception as e:
        return {
            "message": "Error inesperado al crear el delivery.",
            "success": False,
        }