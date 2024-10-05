from fastapi import APIRouter, HTTPException
from controllers.user_controller import *
from models.user_model import User
from fastapi import APIRouter, HTTPException, UploadFile, File

router = APIRouter()
usuario = UserController()


@router.post("/create_user")
async def create_user(user: User):
    try:
        rpta = usuario.create_user(user)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get_user/{user_id}",response_model=User)
async def get_user(user_id: int):
    rpta = usuario.get_user(user_id)
    return rpta

@router.get("/get_users/")
async def get_users():
    rpta = usuario.get_users()
    return rpta


@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int):
    try:
        rpta = usuario.delete_user(user_id)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/update_user/{user_id}")
async def update_user(user_id: int, user: User):
    try:
        rpta = usuario.update_user(user_id, user)
        return rpta
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/create_user_masivo")
async def create_user_masivo(file: UploadFile = File(...)):
    rpta = usuario.create_user_masivo(file) 
    return rpta