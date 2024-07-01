#import config_db
from base_db.config_db import conexion
from datetime import datetime

class Producto:
    # Atributos de clase
    tabla = 'producto'
    campos = ('id','nombre', 'descripcion', 'stock', 'precio_venta', 'fecha', 'imagen')
    conexion = conexion

    # Método constructor
    def __init__(self, id=None, nombre=None, descripcion=None, stock=None, precio_venta=None, fecha=None, imagen=None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock = stock
        self.precio_venta = precio_venta
        self.fecha = fecha
        self.imagen = imagen

    def guardar_db(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        now = datetime.now()
        consulta = f'INSERT INTO {self.tabla} {str(self.campos).replace("\'", "`")} VALUES (%s, %s, %s, %s, %s, %s)'
        datos = (self.nombre, self.descripcion, self.stock, self.precio_venta, self.fecha, self.imagen)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        self.conexion.close()

    @classmethod
    def obtener_todos(cls):
        cls.conexion.connect()
        cursor = cls.conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla}"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cls.conexion.close()
        return datos

    @classmethod
    def obtener_por_id(cls, id):
        cls.conexion.connect()
        cursor = cls.conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla} WHERE id = %s"
        cursor.execute(consulta, (id,))
        dato = cursor.fetchone()
        cls.conexion.close()
        if dato:
            return cls(**dato)
        return None

    def actualizar_db(self):
        self.conexion.connect()
        cursor = self.conexion.cursor()
        consulta = f"""
            UPDATE {self.tabla}
            SET nombre = %s, descripcion = %s, stock = %s, precio_venta = %s, fecha = %s, imagen = %s
            WHERE id = %s
        """
        datos = (self.nombre, self.descripcion, self.stock, self.precio_venta, self.fecha, self.imagen, self.id)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        self.conexion.close()
     # ...
    @classmethod
    def eliminar(cls, id):
        cls.conexion.connect()
        cursor = cls.conexion.cursor()
        consulta = f"DELETE FROM {cls.tabla} WHERE id = %s"
        cursor.execute(consulta, (id,))
        cls.conexion.commit()
        cls.conexion.close()