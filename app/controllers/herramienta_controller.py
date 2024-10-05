import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.herramienta_model import Herramienta

class HerramientaController:

    def create_herramienta(self, herramienta: Herramienta):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO herramienta (tipo, cantidad, id_usuario, disponibles, funcionalidad, estado) VALUES (%s, %s, %s, %s, %s, %s)",
                (herramienta.tipo, herramienta.cantidad, herramienta.id_usuario, herramienta.disponibles, herramienta.funcionalidad, herramienta.estado)
            )
            conn.commit()
            return {"mensaje": "Herramienta creada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                
                conn.close()

    def get_herramienta(self, herramienta_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM herramienta WHERE id = %s", (herramienta_id,))
            result = cursor.fetchone()
            if not result:
                raise HTTPException(status_code=404, detail="Herramienta no encontrada")
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def get_herramientas(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM herramienta")
            result = cursor.fetchall()
            return result
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def delete_herramienta(self, herramienta_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM herramienta WHERE id = %s", (herramienta_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Herramienta no encontrada")
            return {"mensaje": "Herramienta eliminada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

    def update_herramienta(self, herramienta_id: int, herramienta: Herramienta):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE herramienta SET tipo = %s, cantidad = %s, id_usuario = %s, disponibles = %s, funcionalidad = %s, estado = %s  WHERE id = %s",
                (herramienta.tipo, herramienta.cantidad, herramienta.id_usuario, herramienta.disponibles, herramienta.funcionalidad, herramienta_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Herramienta no encontrada o no se realizaron cambios")
            return {"mensaje": "Herramienta actualizada exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=f"Database error: {err}")
        except Exception as err:
            raise HTTPException(status_code=500, detail=f"Unexpected error: {err}")
        finally:
            if conn:
                conn.close()

def get_herramienta_controller():
    return HerramientaController()
