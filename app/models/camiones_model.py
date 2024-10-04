from pydantic import BaseModel

class Camiones(BaseModel):
    id: int = None
    modelo: str
    capacidad: int
    cantidad_herramientas: int




