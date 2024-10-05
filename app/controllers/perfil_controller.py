import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.perfil_model import Perfil
from fastapi.encoders import jsonable_encoder

class PerfilController:

    def create_perfil(self, perfil: Perfil):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO perfil (nombre, descripcion, estado) VALUES (%s, %s, %s)",
                (perfil.nombre, perfil.descripcion, perfil.estado)
            )
            conn.commit()
            return {"mensaje": "Perfil creado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def get_perfil(self, perfil_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM perfil WHERE id = %s", (perfil_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Perfil not found")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def get_perfiles(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM perfil")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def delete_perfil(self, perfil_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM perfil WHERE id = %s", (perfil_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Perfil not found")
            return {"mensaje": "Perfil eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def update_perfil(self, perfil_id: int, perfil: Perfil):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE perfil SET nombre = %s, descripcion = %s, estado = %s WHERE id = %s",
                (perfil.nombre, perfil.descripcion, perfil.estado, perfil_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Perfil no encontrado o no se realizaron cambios")
            return {"mensaje": "Perfil actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()