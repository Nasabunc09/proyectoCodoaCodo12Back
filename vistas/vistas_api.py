from flask import Blueprint, request, jsonify
from componentes.producto import Producto
from componentes.carrito import Carrito
from componentes.modelos import Orden
from componentes.modelos import Orden_Detalle
from componentes.modelos import Persona
from componentes.modelos import Usuario

api = Blueprint('api', __name__)

@api.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    user = Usuario.obtener(email=email)
    if user and user.check_password(password):
        return jsonify({'message': 'Login exitoso', 'user_id': user.id})
    return jsonify({'message': 'Credenciales incorrectas'}), 401

@api.route('/api/register', methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    usuario = Usuario(email, password)
    if usuario.guardar_db():
        return jsonify({'message': 'Registro exitoso'})
    return jsonify({'message': 'Error al registrar usuario'}), 400

@api.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.obtener_todos()
    return jsonify(productos)

@api.route('/api/producto/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = Producto.obtener_por_id(id)
    if producto:
        return jsonify(producto.to_dict())
    return jsonify({'message': 'Producto no encontrado'}), 404

@api.route('/api/producto', methods=['POST'])
def crear_producto():
    data = request.json
    producto = Producto(**data)
    if producto.guardar_db():
        return jsonify({'message': 'Producto creado exitosamente'})
    return jsonify({'message': 'Error al crear producto'}), 400

@api.route('/api/editar_producto/<int:id>', methods=['PUT'])
def editar_producto(id):
    datos = request.json
    producto = Producto.obtener_por_id(id)
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

@api.route('/api/eliminar_producto/<int:id>', methods=['POST'])
def eliminar_producto(id):
  try:
        Producto.eliminar(id)
        return jsonify({'mensaje': 'Producto eliminado exitosamente'})
  except Exception as e:
        return jsonify({'error': str(e)}), 500

@api.route('/api/carrito', methods=['POST'])
def agregar_carrito():
    data = request.json
    carrito = Carrito(**data)
    if carrito.guardar_db():
        return jsonify({'message': 'Producto agregado al carrito'})
    return jsonify({'message': 'Error al agregar producto al carrito'}), 400

@api.route('/api/carrito/<int:idUsuario>', methods=['GET'])
def obtener_carrito(idUsuario):
    productos_carrito = Carrito.obtener_carrito(idUsuario)
    return jsonify(productos_carrito)

@api.route('/api/carrito/<int:idUsuario>/<int:idProducto>', methods=['DELETE'])
def eliminar_carrito(idUsuario, idProducto):
    if Carrito.eliminar_producto(idUsuario, idProducto):
        return jsonify({'message': 'Producto eliminado del carrito'})
    return jsonify({'message': 'Error al eliminar producto del carrito'}), 400

@api.route('/api/orden', methods=['POST'])
def crear_orden():
    data = request.json
    orden = Orden(**data)
    if orden.guardar_db():
        for detalle in data.get('detalles', []):
            orden_detalle = Orden_Detalle(**detalle)
            orden_detalle.guardar_db()
        return jsonify({'message': 'Orden creada exitosamente'})
    return jsonify({'message': 'Error al crear la orden'}), 400


#Mostrar Usuario

@api.route('/api/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios = Usuario.obtener()
    usuarios_dicc = [d.__dict__ for d in usuarios]
    return jsonify(usuarios_dicc)


