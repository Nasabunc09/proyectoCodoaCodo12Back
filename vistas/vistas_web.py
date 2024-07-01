from flask import Blueprint, render_template, request, redirect, url_for, flash
from componentes.producto import Producto

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
