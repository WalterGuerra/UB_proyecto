from fastapi import APIRouter, HTTPException, Depends
from controllers.perfil_controller import *
from models.perfil_model import Perfil

router = APIRouter()

def get_perfil_controller():
    return PerfilController()

@router.post("/create_perfil")
async def create_perfil(perfil: Perfil, perfil_controller: PerfilController = Depends(get_perfil_controller)):
    try:
        rpta = perfil_controller.create_perfil(perfil)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_perfil/{perfil_id}", response_model=Perfil)
async def get_perfil(perfil_id: int, perfil_controller: PerfilController = Depends(get_perfil_controller)):
    try:
        rpta = perfil_controller.get_perfil(perfil_id)
        if not rpta:
            raise HTTPException(status_code=404, detail="Perfil not found")
        return rpta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_perfiles/")
async def get_perfiles(perfil_controller: PerfilController = Depends(get_perfil_controller)):
    try:
        rpta = perfil_controller.get_perfiles()
        return rpta
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_perfil/{perfil_id}")
async def delete_perfil(perfil_id: int, perfil_controller: PerfilController = Depends(get_perfil_controller)):
    try:
        rpta = perfil_controller.delete_perfil(perfil_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_perfil/{perfil_id}")
async def update_perfil(perfil_id: int, perfil: Perfil, perfil_controller: PerfilController = Depends(get_perfil_controller)):
    try:
        rpta = perfil_controller.update_perfil(perfil_id, perfil)
        if not rpta:
            raise HTTPException(status_code=404, detail="Perfil no encontrado o no se realizaron cambios")
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))