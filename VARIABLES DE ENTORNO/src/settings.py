#creamos una clase para gestionar las variables de entorno
from dotenv import load_dotenv
from dataclasses import dataclass
import os
from typing import Optional
@dataclass
class Settings:
    MY_SQL_USER: str
    #MY_SQL_PASSWORD: str#opcional la ponemos en última posición
    MY_SQL_DB: str
    MY_SQL_PASSWORD: Optional[str] = 'guay'


load_dotenv()

MY_SQL_USER = os.getenv('MY_SQL_USER')
MY_SQL_PASSWORD = os.getenv('MY_SQL_PASSWORD')
MY_SQL_DB = os.getenv('MY_SQL_HOST')

settings = Settings(MY_SQL_USER = MY_SQL_USER, 
                    MY_SQL_PASSWORD = MY_SQL_PASSWORD, #quitamos este parámetro y ejecutamos para ver que la contraseña es requerida.
                    MY_SQL_DB = MY_SQL_DB)

