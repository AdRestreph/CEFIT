import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

class DatabaseConnection:
    """Clase para conectar con la base de datos"""

    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.database = os.getenv("DB_NAME")
        self.port = int(os.getenv("DB_PORT", 3306))

        self.connection = None

    def connect(self):
        """Crea una conexion con la base de datos y retorna el resultado de la conexion"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port,
                use_pure = True
            )

            if self.connection.is_connected():
                print(" Conexion exitosa")
                return True

        except Error as e:
            print(f" Error al conectar: {e}")
            return False

    def disconnect(self):
        """Cierra la conexion con la base de datos"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print(" Conexión cerrada")

    def get_connection(self):
        return self.connection