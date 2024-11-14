from pydantic import BaseModel
from typing import List
from src.models import Roles
from datetime import date

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