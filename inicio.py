import pprint
from producto import Producto

pp = pprint.PrettyPrinter(indent=4)

datos = Producto.obtener_todos()

pp.pprint(datos)

