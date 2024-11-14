from pony.orm import db_session, desc, select
from fastapi import HTTPException, Query
from typing import Optional
from uuid import UUID
import bcrypt
from pony.orm.core import TransactionIntegrityError
from src import models, schemas

class UsersService:
    def __init__(self):
        pass

    def create_user(self, user: schemas.UserCreate) -> dict:
        with db_session:
            try:
                usuario = models.User(
                    username = user.username, 
                    password = self.hash_password(user.password),
                    role = user.role,
                )
                print("Usuario creado correctamente.")
                user_dict = usuario.to_dict(exclude=['id'])
                return user_dict
            except TransactionIntegrityError as e:
                print(f"Error de integridad transaccional: {e}")
                raise HTTPException(
                    status_code=400, detail="Error de integridad al crear el usuario.")
            except Exception as e:
                print(f"Error al crear el usuario: {e}")
                raise HTTPException(
                    status_code=500, detail="Error al crear el usuario.")
    
    def search_user(self, username: Optional[str], password: str) -> models.User:
        with db_session:
            user = select(u for u in models.User if (
                u.username == username)).first()
            
            if not user:
                raise HTTPException(
                status_code=404, detail="Usuario no encontrado")
            
            password_is_valid = self.check_password(user.password, password)

            if not password_is_valid:
                raise HTTPException(
                    status_code=401, detail="Contraseña incorrecta"
                )
            
            return user
    
    def search_user_by_id(self, user_id: str):
        with db_session:
            try:
                user = select(u for u in models.User if u.id == user_id).first()
                return user if user else None
            except Exception as e:
                return None

    @staticmethod
    def hash_password(password: str) -> str:
        # Generar una sal (salt)
        salt = bcrypt.gensalt()
        # Encriptar la contraseña con la sal 
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    @staticmethod
    def check_password(stored_password: str, provided_password: str ) -> bool:
        # Comparar la contraseña proporcionada con la almacenada
        return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))
    
    #Credenciales ADMIN
    # {
    # "username": "moreno",
    # "password": "123",
    # "role": "ADMIN"
    # }