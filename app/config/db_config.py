import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="b3mov0t24gltgdymhcr2-mysql.services.clever-cloud.com",
        user="upmb4w1ymjlodhzn",
        password="jSrLN9cQYS1GVU54lSdq",
        database="b3mov0t24gltgdymhcr2"
    )