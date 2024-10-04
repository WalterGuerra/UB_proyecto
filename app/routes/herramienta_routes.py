from fastapi import APIRouter, HTTPException, Depends
from controllers.herramienta_controller import *
from models.herramienta_model import Herramienta

router = APIRouter()

@router.post("/create_herramienta")
async def create_herramienta(herramienta: Herramienta, herramienta_controller: HerramientaController = Depends(get_herramienta_controller)):
    try:
        return herramienta_controller.create_herramienta(herramienta)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_herramienta/{herramienta_id}")
async def get_herramienta(herramienta_id: int, herramienta_controller: HerramientaController = Depends(get_herramienta_controller)):
    try:
        return herramienta_controller.get_herramienta(herramienta_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/get_herramientas")
async def get_herramientas(herramienta_controller: HerramientaController = Depends(get_herramienta_controller)):
    try:
        return herramienta_controller.get_herramientas()
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/delete_herramienta/{herramienta_id}")
async def delete_herramienta(herramienta_id: int, herramienta_controller: HerramientaController = Depends(get_herramienta_controller)):
    try:
        return herramienta_controller.delete_herramienta(herramienta_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_herramienta/{herramienta_id}")
async def update_herramienta(herramienta_id: int, herramienta: Herramienta, herramienta_controller: HerramientaController = Depends(get_herramienta_controller)):
    try:
        return herramienta_controller.update_herramienta(herramienta_id, herramienta)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
