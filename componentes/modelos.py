from base_db.tabla_db import Tabla
from base_db.conexion_db import conexion as con
from auxiliares.cifrado import encriptar

class Producto(Tabla):
    tabla = 'producto'
    conexion = con
    campos = ('id', 'nombre', 'descripcion', 'stock', 'precio_venta', 'fecha')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Domicilio(Tabla):
    tabla = 'domicilio'
    conexion = con
    campos = ('id', 'idUsuario', 'calle', 'provincia', 'ciudad', 'numero', 'pais', 'codigoPostal')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Carrito(Tabla):
    tabla = 'carrito'
    conexion = con
    campos = ('id', 'idUsuario', 'idProducto', 'cantidad')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Orden(Tabla):
    tabla = 'orden'
    conexion = con
    campos = ('id', 'idUsuario', 'idMetodoPago', 'total', 'fecha')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class Orden_Detalle(Tabla):
    tabla = 'orden_detalle'
    conexion = con
    campos = ('id', 'idOrden', 'idProducto', 'cantidad', 'precio')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

class C_Metodo_Pago(Tabla):
    tabla = 'c_metodo_pago'
    conexion = con
    campos = ('id', 'nombre')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Imagen(Tabla):
    tabla = 'imagen'
    conexion = con
    campos = ('id', 'idProducto', 'url_img', 'texto_alt')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Persona(Tabla):
    tabla = 'persona'
    conexion = con
    campos = ('id', 'idUsuario', 'idDomicilio','nombre', 'apellido', 'dni', 'telefono')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Usuario(Tabla):
    tabla = 'usuario'
    conexion = con
    campos = ('id', 'email', 'password', 'fecha')
    
    def __init__(self, *args, de_bbdd=False):
        if not de_bbdd:
            cuenta = []
            cuenta.append(args[0])
            cuenta.append(encriptar(args[1]))
            super().crear(tuple(cuenta), de_bbdd)
        else:
            super().crear(args, de_bbdd)

    @classmethod
    def autenticar(cls, email, password):
        hashed_password = encriptar(password)
        consulta = f"SELECT * FROM {cls.tabla} WHERE email = %s AND password = %s"
        #resultado = cls.__conectar(consulta, (email, hashed_password))
        resultado = cls._Tabla__conectar(consulta, (email, hashed_password))
        if resultado:
            return resultado[0]
        return None
