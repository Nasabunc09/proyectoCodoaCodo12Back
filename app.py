from flask import Flask


app = Flask (__name__)

@app.route('/')
def inicio():
    return "Bienvenido Flask"

if __name__ == "main":
    app.run()

