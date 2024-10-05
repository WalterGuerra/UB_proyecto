from pydantic import BaseModel

class User(BaseModel):
    id: int = None
    usuario: str
    contrasena: str
    nombre: str
    apellido: str
    documento: str
    telefono: str
    idperfil: int
    idcamiones: int
   