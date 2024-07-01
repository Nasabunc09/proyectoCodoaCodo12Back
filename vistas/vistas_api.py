from flask import Blueprint, jsonify, request

from componentes.modelos import Producto
from componentes.modelos import Usuario
from componentes.modelos import Persona

api = Blueprint('api-sweet_candy', __name__)

@api.route('/api-sweet_candy/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.obtener()
    return jsonify(productos)

@api.route('/api-sweet_candy/productos', methods=['POST'])
def agregar_producto():
    datos = request.json
    nuevo_producto = Producto(
        nombre=datos['nombre'],
        descripcion=datos['descripcion'],
        stock=datos['stock'],
        precio_venta=datos['precio_venta'],
        fecha=datos['fecha'],
        imagen=datos['imagen']
    )
    nuevo_producto.guardar_db()
    return jsonify({"mensaje": "Producto agregado exitosamente"}), 201

@api.route('/api/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    datos = request.json
    producto = Producto.actualizar(id)
    if producto:
        producto.nombre = datos.get('nombre', producto.nombre)
        producto.descripcion = datos.get('descripcion', producto.descripcion)
        producto.stock = datos.get('stock', producto.stock)
        producto.precio_venta = datos.get('precio_venta', producto.precio_venta)
        producto.fecha = datos.get('fecha', producto.fecha)
        producto.imagen = datos.get('imagen', producto.imagen)
        producto.actualizar_db()
        return jsonify({"mensaje": "Producto actualizado exitosamente"})
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@api.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
  try:
        Producto.eliminar(id)
        return jsonify({'mensaje': 'Producto eliminado exitosamente'})
  except Exception as e:
        return jsonify({'error': str(e)}), 500
<<<<<<< HEAD
@api.route('/api/carrito', methods=['POST'])
def agregar_carrito():
    id_usuario = request.form.get('idUsuario')
    id_producto = request.form.get('idProducto')
    cantidad = request.form.get('cantidad')

    if not id_usuario or not id_producto or not cantidad:
        return jsonify({"error": "Datos incompletos"}), 400

    carrito = Carrito(idUsuario=id_usuario, idProducto=id_producto, cantidad=cantidad)
    carrito.agregar_db()

    return jsonify({"mensaje": "Producto añadido al carrito"}), 201  
=======

#Crear Usuario
@api.route("/api-sweet_candy/Usuario", methods=['POST'])
def crear_cuenta():
    
    if request.method == 'POST':
        datos = request.json["datos"]
        cta_nueva = Usuario(
            datos['email'],
            datos['password'],
        )
        
        respuesta = {}
        
        try:
            cta_nueva.guardar_db()
            respuesta['mensaje'] = 'Cuenta creada con éxito!'
            respuesta['status'] = 200
        except Exception as e:
            respuesta['mensaje'] = 'No se puedo crear la cuenta!'
            respuesta['status'] = 409
            
    else:
        respuesta['mensaje'] = 'No se recibieron datos.'
        respuesta['status'] = 204    

    return jsonify(respuesta)

@api.route('/api-sweet_candy/validar', methods=['POST'])
def validar_cuenta():
    respuesta = {}    
    
    if request.method == 'POST':
        datos = request.json["datos"]
        ingreso = Usuario(datos['email'], datos['password'])
        cuenta = Usuario.obtener('email', datos['email'])
        
        
        if cuenta and ingreso.clave == cuenta.clave:
            persona = Persona.obtener('id', cuenta.id)

            if not persona:
                respuesta['perfil'] = 0
            else:
                respuesta['perfil'] = 1
            
            respuesta['mensaje'] = 'Ingreso exitoso!'
            respuesta['status'] = 200
        else:
            respuesta['mensaje'] = 'Verifique los datos enviados.'
            respuesta['status'] = 409
    
    return jsonify(respuesta)

@api.route('/api-sweet_candy/obt-perfil', methods=['POST'])
def obtener_perfil():
    
    if request.method == 'POST':
        correo = request.json['datos']
        cuenta = Usuario.obtener('email', correo)
        perfil = Persona.obtener('idUsuario', cuenta.id)
        perfil = perfil.__dict__
        perfil['email'] = cuenta.correo
        del perfil['id']
        del perfil['idUsuario']
    
    return jsonify(perfil)    

@api.route('/api-sweet_candy/eliminar', methods=['DELETE'])
def eliminar_cta_perfil():
    
    if request.method == 'DELETE':
        datos = request.json["datos"]
        cuenta = Usuario.obtener('email', datos)
        
        eliminar_perfil = Persona.eliminar(cuenta.id)
        eliminar_cuenta = Usuario.eliminar(cuenta.id)
        
        if eliminar_cuenta == eliminar_perfil:
            respuesta = {'mensaje': eliminar_perfil}
        else:
            respuesta = {'mensaje': 'Algo salió mal!'}
    
    else:
        respuesta = {'mensaje': 'no se recibieron datos.'}
        
    return jsonify(respuesta)
>>>>>>> f4e127e9a4c4d13039c1504c5b1d703c2676a674
