#Crea usuarios
def validar_nombre(dato_str):

    if dato_str.isalpha():
        return True
    
    return False

def crear_usuario():
    nombre = input("Ingrese su nombre: ")

    if validar_nombre(nombre):
        print("Se creó el usuario: {nombre}")

    else:      

        print("Dato inválido como nombre")

def guardar_db():
    pass