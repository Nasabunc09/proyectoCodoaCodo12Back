
from flask import Blueprint, render_template, request, redirect, url_for, flash,session
from componentes.producto import Producto
from componentes.carrito import Carrito
from componentes.modelos import Orden
from componentes.modelos import Orden_Detalle
from componentes.modelos import Usuario

web = Blueprint('web', __name__)

@web.route('/')
def index():
    productos = Producto.obtener_todos()
    return render_template('index.html', productos=productos)

@web.route('/producto/<int:id>')
def ver_producto(id):
    producto = Producto.obtener_por_id(id)
    if producto:
        return render_template('ver_producto.html', producto=producto)
    return redirect(url_for('web.index'))

@web.route('/editar_producto/<int:id>', methods=['GET', 'POST'])
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

@web.route('/usuarios')
def usuarios():
    usuario = Usuario.obtener()
    usuario = [d.__dict__ for d in usuario]
    return render_template('usuarios.html', usuario=usuario)

@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario.autenticar(email, password)
        if usuario:
            session['user_id'] = usuario.id
            return redirect(url_for('web.index'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')
    return render_template('login.html')

@web.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        usuario = Usuario(email, password)
        if usuario.guardar_db():
            flash('Registro exitoso', 'success')
            return redirect(url_for('web.login'))
        flash('Error al registrar usuario', 'danger')
    return render_template('registro.html')

@web.route('/carrito')
def ver_carrito():
    user_id = session.get('user_id')
    if user_id:
        productos_carrito = Carrito.obtener_carrito(user_id)
        return render_template('carrito.html', productos_carrito=productos_carrito)
    else:
        flash('Debes iniciar sesión para ver tu carrito', 'error')
        return redirect(url_for('web.login'))
    
@web.route('/carrito/agregar', methods=['POST'])
def agregar_carrito():
    user_id = session.get('user_id')
    if user_id:
        idProducto = request.form['idProducto']
        cantidad = request.form['cantidad']
        carrito = Carrito(user_id, idProducto, cantidad)
        carrito.agregar_db()
        flash('Producto agregado al carrito', 'success')
        return redirect(url_for('web.ver_carrito'))
    else:
        flash('Debes iniciar sesión para agregar productos al carrito', 'error')
        return redirect(url_for('web.login'))
"""
def ver_carrito():
    # Assume the user is logged in and has a user_id in session
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('web.login'))
    
    productos_carrito = Carrito.obtener_carrito(user_id)
    return render_template('carrito.html', productos_carrito=productos_carrito)
"""
@web.route('/carrito/eliminar/<int:idProducto>', methods=['POST'])
def eliminar_del_carrito(idProducto):
    user_id = session.get('user_id')
    if user_id:
        Carrito.eliminar_producto(user_id, idProducto)
        flash('Producto eliminado del carrito', 'success')
        return redirect(url_for('web.ver_carrito'))
    else:
        flash('Debes iniciar sesión para eliminar productos del carrito', 'error')
        return redirect(url_for('web.login'))
@web.route('/orden/crear', methods=['POST'])
def crear_orden():
    user_id = session.get('user_id')
    if user_id:
        metodo_pago = request.form['metodo_pago']
        productos_carrito = Carrito.obtener_carrito(user_id)
        total = sum(item['cantidad'] * item['precio_venta'] for item in productos_carrito)

        orden = Orden(user_id, metodo_pago, total)
        orden.guardar_db()

        for item in productos_carrito:
            orden_detalle = Orden_Detalle(orden.id, item['idProducto'], item['cantidad'], item['precio_venta'])
            orden_detalle.guardar_db()

        Carrito.eliminar_carrito(user_id)
        flash('Pedido realizado con éxito', 'success')
        return redirect(url_for('web.index'))
    else:
        flash('Debes iniciar sesión para realizar un pedido', 'error')
        return redirect(url_for('web.login'))    
"""
@web.route('/orden', methods=['POST'])
def crear_orden():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('web.login'))

    carrito = Carrito.obtener_carrito(user_id)
    if not carrito:
        flash('El carrito está vacío', 'danger')
        return redirect(url_for('web.ver_carrito'))

    total = sum(item['precio_venta'] * item['cantidad'] for item in carrito)
    orden = Orden(idUsuario=user_id, idMetodoPago=request.form['metodo_pago'], total=total)
    
    if orden.guardar_db():
        for item in carrito:
            detalle = Orden_Detalle(idOrden=orden.id, idProducto=item['idProducto'], cantidad=item['cantidad'], precio=item['precio_venta'])
            detalle.guardar_db()
        flash('Orden creada exitosamente', 'success')
    else:
        flash('Error al crear la orden', 'danger')

    return redirect(url_for('web.ver_carrito'))

"""





"""
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