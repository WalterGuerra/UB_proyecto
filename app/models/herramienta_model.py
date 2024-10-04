from pydantic import BaseModel

class Herramienta(BaseModel):
    id: int = None
    tipo: str
    cantidad: int
    id_usuario: int
    disponibles: int
    funcionalidad: str
   
  
