import config_db
from datetime import datetime

class Producto:

    #Atributos de clase
    tabla = 'producto'
    campos = ('nombre', 'descripcion', 'stock', 'precio_venta', 'fecha', 'imagen')
    conexion = config_db.conexion

    #Metodo constructor
    def __init__(self,nombre,descripcion,stock,precio_venta,fecha,imagen):

        #Atributo de instancia
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
        consulta = f'INSERT INTO {self.tabla} {str(self.campos).replace("'","`")} VALUES (%s, %s, %s, %s, %s, %s)'
        datos = (self.nombre, self.descripcion, self.stock, self.precio_venta, self.fecha, self.imagen)
        cursor.execute(consulta, datos)
        self.conexion.commit()
        self.conexion.close()

#agregar producto
#producto = Producto("caramelos de miel", "caramelos blandos sweet honey", '3', '1000', 'now', "miel.jfif")
#producto.guardar_db()


    @classmethod
    def obtener_todos(cls):
        cls.conexion.connect()
        cursor = cls.conexion.cursor(dictionary=True)
        consulta = f"SELECT * FROM {cls.tabla}"
        cursor.execute(consulta)
        datos = cursor.fetchall()
        cls.conexion.close()
        return datos
    
print(Producto.obtener_todos())
        
    #
        
    # @classmethod
    # def actualizar(cls, id, nombre, apellido, cuit):
    #     # ...
    #     consulta = f"UPDATE {cls.tabla} WHERE id = %s SET nombre = %s ... ;"
    #     datos = (id, nombre, apellido, cuit)
    #     cursor.execute(consulta.datos)
    #     # ...