from flask import Flask
from flask import jsonify
from componentes.producto import obtener_todos

app = Flask (__name__)

@app.route('/')
def inicio():
    return "Bienvenido Flask"

@app.route('/api/test') # http://127.0.0.1:5000/api/test
def mostrar_datos():
    # return obtener_datos() # 'idTest', pero necesito "idTest"
    return jsonify(obtener_todos()) # 'idTest', pero necesito "idTest"

if __name__ == "main":
    app.run()

