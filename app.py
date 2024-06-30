from create_app import create_app

app = create_app()

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
from componentes.vistas_api import api

app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)

"""


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


app = Flask (__name__)

@app.route('/')
def inicio():
    return "Bienvenido Flask"

if __name__ == "main":
    app.run()

"""