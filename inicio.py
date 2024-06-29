import pprint
#from componentes.producto import Producto
from componentes.config_db import conexion

pp = pprint.PrettyPrinter(indent=4)

datos = Producto.obtener_todos()

pp.pprint(datos)

