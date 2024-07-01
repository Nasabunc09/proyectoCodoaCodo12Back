from flask import Blueprint, render_template, request, redirect, url_for, flash
from componentes.producto import Producto
from componentes.carrito import Carrito
web = Blueprint('web', __name__)


@web.route('/')
def index():
    productos = Producto.obtener_todos()
    return render_template('index.html', productos=productos)

@web.route('/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    stock = request.form['stock']
    precio_venta = request.form['precio_venta']
    fecha = request.form['fecha']
    imagen = request.form['imagen']

    nuevo_producto = Producto(nombre, descripcion, stock, precio_venta, fecha, imagen)
    nuevo_producto.guardar_db()
    
    flash("Producto agregado exitosamente")
    return redirect(url_for('web.index'))

@web.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.obtener_por_id(id)
    if not producto:
        flash("Producto no encontrado")
        return redirect(url_for('web.index'))
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.stock = request.form['stock']
        producto.precio_venta = request.form['precio_venta']
        producto.fecha = request.form['fecha']
        producto.imagen = request.form['imagen']
        
        producto.actualizar_db()
        
        flash("Producto actualizado exitosamente")
        return redirect(url_for('web.index'))
    
    return render_template('editar_producto.html', producto=producto)

@web.route('/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    producto = Producto.obtener_por_id(id)
    if producto:
        producto.eliminar_db()
    return redirect(url_for('web.index'))
# Ruta para mostrar el carrito

@web.route('/carrito')
def ver_carrito():
    id_usuario = 1  # Aquí podrías obtener el id del usuario autenticado
    productos_carrito = Carrito.obtener_carrito(id_usuario)
    return render_template('carrito.html', carrito=productos_carrito)

@web.route('/carrito/agregar', methods=['POST'])
def agregar_al_carrito():
    id_usuario = 1  # Aquí podrías obtener el id del usuario autenticado
    id_producto = request.form['idProducto']
    cantidad = request.form['cantidad']
    carrito_item = Carrito(idUsuario=id_usuario, idProducto=id_producto, cantidad=cantidad)
    carrito_item.agregar_db()
    flash('Producto agregado al carrito')
    return redirect(url_for('web.ver_carrito'))

@web.route('/carrito/eliminar/<int:idProducto>', methods=['POST'])
def eliminar_del_carrito(idProducto):
    id_usuario = 1  # Aquí podrías obtener el id del usuario autenticado
    Carrito.eliminar_producto(id_usuario, idProducto)
    flash('Producto eliminado del carrito')
    return redirect(url_for('web.ver_carrito'))

"""
@web.route('/carrito')
def ver_carrito():
    idUsuario = 1  # Este debería ser el ID del usuario autenticado
    productos_carrito = Carrito.obtener_carrito(idUsuario)
    return render_template('carrito.html', productos=productos_carrito)
# Ruta para agregar producto al carrito

@web.route('/agregar_carrito/<int:idProducto>', methods=['POST'])
def agregar_carrito(idProducto):
    idUsuario = 1  # Este debería ser el ID del usuario autenticado
    cantidad = request.form['cantidad']
    carrito = Carrito(idUsuario, idProducto, int(cantidad))
    carrito.agregar_producto()
    flash('Producto agregado al carrito')
    return redirect(url_for('web.index'))



# Ruta para eliminar producto del carrito
@web.route('/eliminar_carrito/<int:idProducto>', methods=['POST'])
def eliminar_carrito(idProducto):
    idUsuario = 1  # Este debería ser el ID del usuario autenticado
    Carrito.eliminar_producto(idUsuario, idProducto)
    flash('Producto eliminado del carrito')
    return redirect(url_for('web.ver_carrito'))"""