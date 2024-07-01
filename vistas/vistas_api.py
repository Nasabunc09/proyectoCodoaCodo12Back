from flask import Blueprint, jsonify, request
from componentes.producto import Producto

api = Blueprint('api', __name__)

@api.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = Producto.obtener_todos()
    return jsonify(productos)

@api.route('/api/productos', methods=['POST'])
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

@api.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
  try:
        Producto.eliminar(id)
        return jsonify({'mensaje': 'Producto eliminado exitosamente'})
  except Exception as e:
        return jsonify({'error': str(e)}), 500
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
