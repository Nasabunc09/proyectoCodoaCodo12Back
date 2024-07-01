from flask import Flask
from vistas.vistas_api import api as api_blueprint
from vistas.vistas_web import web as web_blueprint

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"

    # Registrar Blueprints
    app.register_blueprint(api_blueprint)
    app.register_blueprint(web_blueprint)

    return app

"""
from flask import Flask, render_template
from flask_cors import CORS
from componentes.vistas_api import api

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(api)

    @app.route('/')
    def inicio():
        return render_template('index.html')

    return app
"""