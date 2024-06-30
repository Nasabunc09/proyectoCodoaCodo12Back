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
