import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.user_model import User
from fastapi.encoders import jsonable_encoder

class UserController:


    def create_user(self, user: User):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO usuario (usuario, contrasena, nombre, apellido, documento, telefono, idperfil, idcamiones) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (user.usuario, user.contrasena, user.nombre, user.apellido, user.documento, user.telefono, user.idperfil, user.idcamiones)  
            )
            conn.commit()
            return {"mensaje": "Usuario creado exitosamente"}
        except Exception as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()



    def get_user(self, user_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (user_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id': result[0],
                    'usuario': result[1],
                    'contrasena': result[2],
                    'nombre': result[3],
                    'apellido': result[4],
                    'documento': result[5],
                    'telefono': result[6],
                    'idperfil': result[7],
                    'idcamiones': result[8]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def get_users(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            result = cursor.fetchall()
            payload = []

            for data in result:
                content = {
                    'id': data[0],
                    'usuario': data[1],
                    'contrasena': data[2],
                    'nombre': data[3],
                    'apellido': data[4],
                    'documento': data[5],
                    'telefono': data[6],
                    'idperfil': data[7],
                    'idcamiones': data[8]
                }
                payload.append(content)

            return {"resultado": jsonable_encoder(payload)}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def update_user(self, user_id: int, user: User):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE usuario SET usuario = %s, contrasena = %s, nombre = %s, apellido = %s, documento = %s, telefono = %s, idperfil = %s, idcamiones = %s WHERE id = %s",
                (user.usuario, user.contrasena, user.nombre, user.apellido, user.documento, user.telefono, user.idperfil, user.idcamiones, user_id)
            )
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario actualizado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()

    def delete_user(self, user_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM usuario WHERE id = %s", (user_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return {"mensaje": "Usuario eliminado exitosamente"}
        except mysql.connector.Error as err:
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()