from pony.orm import * 
from src.db import db
from enum import Enum
from datetime import date


class Roles(str, Enum):
    ADMIN = "ADMIN"

class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    username = Required(str)
    password = Required(str)
    role = Required(str)

    _table_ = "Usuario"