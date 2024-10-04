from fastapi import APIRouter, HTTPException
from models.camiones_model import Camiones
from controllers.camiones_controller import CamionesController

router = APIRouter()
controller = CamionesController()

@router.post("/camiones/", response_model=dict)
async def crear_camion(camion: Camiones):
    try:
        return controller.create_camion(camion)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/camiones/{camion_id}", response_model=dict)
async def obtener_camion(camion_id: int):
    try:
        return controller.get_camion(camion_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/camiones/", response_model=dict)
async def obtener_camiones():
    try:
        return controller.get_camiones()
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/camiones/{camion_id}", response_model=dict)
async def actualizar_camion(camion_id: int, camion: Camiones):
    try:
        return controller.update_camion(camion_id, camion)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/camiones/{camion_id}", response_model=dict)
async def eliminar_camion(camion_id: int):
    try:
        return controller.delete_camion(camion_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
