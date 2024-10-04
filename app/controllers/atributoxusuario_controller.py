import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.atributoxusuario_model import Atributoxusuario
from fastapi.encoders import jsonable_encoder



class AtributoxusuarioController:

    def create_atributoxusuario(self, atributoxusuario: Atributoxusuario):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO atributoxusuario (idusuario, idatriduto, valor, descripcion) VALUES (%s, %s, %s, %s)",
                (atributoxusuario.idusuario, atributoxusuario.idatriduto, atributoxusuario.valor, atributoxusuario.descripcion)
            )
            conn.commit()
            return {"mensaje": "Atributoxusuario creado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_atributoxusuario(self, atributoxusuario_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': result[0],
                    'idusuario': result[1],
                    'idatriduto': result[2],
                    'valor': result[3],
                    'descripcion': result[4]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Atributoxusuario no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_atributoxusuarios(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributoxusuario")
            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    'id': data[0],
                    'idusuario': data[1],
                    'idatriduto': data[2],
                    'valor': data[3],
                    'descripcion': data[4]
                }
                payload.append(content)

            return {"resultado": jsonable_encoder(payload)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_atributoxusuario(self, atributoxusuario_id: int, atributoxusuario: Atributoxusuario):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE atributoxusuario SET idusuario = %s, idatriduto = %s, valor = %s, descripcion = %s WHERE id = %s",
                (atributoxusuario.idusuario, atributoxusuario.idatriduto, atributoxusuario.valor, atributoxusuario.descripcion, atributoxusuario_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributoxusuario no encontrado")
            return {"mensaje": "Atributoxusuario actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_atributoxusuario(self, atributoxusuario_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM atributoxusuario WHERE id = %s", (atributoxusuario_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Atributoxusuario no encontrado")
            return {"mensaje": "Atributoxusuario eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
