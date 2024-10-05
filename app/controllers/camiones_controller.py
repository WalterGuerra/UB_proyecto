import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.camiones_model import Camiones
from fastapi.encoders import jsonable_encoder

class CamionesController:

    def create_camion(self, camion: Camiones):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO camiones (modelo, capacidad, cantidad_herramientas, estado) VALUES (%s, %s, %s, %s)",
                (camion.modelo, camion.capacidad, camion.cantidad_herramientas)
            )
            conn.commit()
            return {"mensaje": "Camión creado exitosamente"}
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_camion(self, camion_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM camiones WHERE id = %s", (camion_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': result[0],
                    'modelo': result[1],
                    'capacidad': result[2],
                    'cantidad_herramientas': result[3],
                    'estado': result[4]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Camión no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_camiones(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM camiones")
            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    'id': data[0],
                    'modelo': data[1],
                    'capacidad': data[2],
                    'cantidad_herramientas': data[3],
                    'estado': data[4]
                }
                payload.append(content)

            return {"resultado": jsonable_encoder(payload)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_camion(self, camion_id: int, camion: Camiones):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE camiones SET modelo = %s, capacidad = %s, cantidad_herramientas = %s, estado = %s WHERE id = %s",
                (camion.modelo, camion.capacidad, camion.cantidad_herramientas, camion_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Camión no encontrado")
            return {"mensaje": "Camión actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_camion(self, camion_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM camiones WHERE id = %s", (camion_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Camión no encontrado")
            return {"mensaje": "Camión eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
