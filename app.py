<<<<<<< HEAD
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.json.ensure_ascii = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Importar las vistas (rutas)
from componentes.vistas_web import *
from componentes.vistas_api import api

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)




"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.json.ensure_ascii = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Importar las vistas (rutas)
from componentes.vistas_web import *

if __name__ == "__main__":
    app.run(debug=True)


"""

"""

from flask import Flask
=======
>>>>>>> daniela

from flask import Flask, render_template, request, redirect, url_for, flash
from componentes.producto import Producto

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    productos = Producto.obtener_todos()
    return render_template('index.html', productos=productos)

@app.route('/agregar', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    descripcion = request.form['descripcion']
    stock = request.form['stock']
    precio_venta = request.form['precio_venta']
    fecha = request.form['fecha']
    imagen = request.form['imagen']

<<<<<<< HEAD
"""
=======
    nuevo_producto = Producto(nombre, descripcion, stock, precio_venta, fecha, imagen)
    nuevo_producto.guardar_db()
    
    flash("Producto agregado exitosamente")
    return redirect(url_for('index'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = Producto.obtener_por_id(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.stock = request.form['stock']
        producto.precio_venta = request.form['precio_venta']
        producto.fecha = request.form['fecha']
        producto.imagen = request.form['imagen']
        
        producto.actualizar_db()
        
        flash("Producto actualizado exitosamente")
        return redirect(url_for('index'))
    
    return render_template('editar_producto.html', producto=producto)

@app.route('/eliminar/<int:id>')
def eliminar_producto(id):
    Producto.eliminar_db(id)
    
    flash("Producto eliminado exitosamente")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



"""

from create_app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)


"""
>>>>>>> daniela
