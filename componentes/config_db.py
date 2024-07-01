import mysql.connector

class ConexionDB:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sweet_candy"
        )

    def cursor(self, dictionary=False):
        if dictionary:
            return self.connection.cursor(dictionary=True)
        return self.connection.cursor()

    def commit(self):
        if self.connection:
            self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()

conexion = ConexionDB()
