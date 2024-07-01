# componentes/carrito.py
from componentes.config_db import conexion

class Carrito:
    tabla = 'carrito'

    def __init__(self, idUsuario=None, idProducto=None, cantidad=None):
        self.idUsuario = idUsuario
        self.idProducto = idProducto
        self.cantidad = cantidad

    def agregar_db(self):
        conexion.connect()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO carrito (idUsuario, idProducto, cantidad) VALUES (%s, %s, %s)",
            (self.idUsuario, self.idProducto, self.cantidad)
        )
        conexion.commit()
        conexion.close()

    @classmethod
    def obtener_carrito(cls, idUsuario):
        conexion.connect()
        cursor = conexion.cursor(dictionary=True)
        consulta = f'SELECT c.*, p.nombre, p.precio_venta FROM {cls.tabla} c JOIN producto p ON c.idProducto = p.id WHERE idUsuario = %s'
        cursor.execute(consulta, (idUsuario,))
        datos = cursor.fetchall()
        conexion.close()
        return datos

    @classmethod
    def eliminar_producto(cls, idUsuario, idProducto):
        conexion.connect()
        cursor = conexion.cursor()
        consulta = f'DELETE FROM {cls.tabla} WHERE idUsuario = %s AND idProducto = %s'
        cursor.execute(consulta, (idUsuario, idProducto))
        conexion.commit()
        conexion.close()
