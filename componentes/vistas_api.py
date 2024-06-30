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

# Agregar más rutas para actualizar y eliminar productos según sea necesario


# Agregar más rutas para actualizar y eliminar productos según sea necesario
