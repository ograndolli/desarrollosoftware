# -*- coding: utf-8 -*-
# TODO #1a: importar  el modulo db_productos

productos = []
# TODO #1b: cargar la lista de productos con la función
#          cargar_productos() del módulo db_productos.

# TODO #2: definir una función mostrar_productos()
#          que reciba la lista de productos, no retorne nada,
#          y muestre la lista utilizando el siguiente formato para cada producto:
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# "Producto {id}"
# "{nombre} ${precio}"
# "---"
# ...

# TODO #3: definir una función calcular_precio_actualizado()
#          que reciba: el precio anterior y porcentaje de aumento
#          y retorne: el precio con el aumento.

# TODO #4: Crear una función actualizar_precios() que reciba la lista de productos y 
#          el porcentaje de aumento. La función debe recorrer cada producto de la
#          lista e invocar calcular_precio_actualizado() (a la cual tendrá que pasarle
#          el precio del producto y el porcentaje de aumento) para obtener el precio
#          actualizado y modifique la lista "in-place" actualizando el precio de cada
#          producto. La función no debe retornar nada sino dejar modificada la lista
#          pasada por el usuario.

"""
if __name__ == '__main__':
    # TODO #5a: mostrar la lista cargada
    # TODO #5b: el usuario debe ingresar el porcentaje de aumento
    # TODO #5c: usar la función actualizar_precios() para actualizar los precios de la lista
    # TODO #5d: mostrar la lista con los precios actualizados

"""
import db_productos
#TODO1

productos = db_productos.cargar_productos()
print(productos)

#TODO2

def mostrar_productos(productos): 
    for elem in productos:
        print(f"Producto {elem['id']}")
        print(f"{elem ['nombre: ']}")
        print(f"${elem ['precio: ']}")


mostrar_productos(productos)

#TODO3 y TODO4


def calcular_precio_actualizado(a, p):
    pact=(p*a/100)+p
    return(pact)


aumento=float(input("Ingrese el porcentaje de aumento: "))
precio=float(input("Ingrese el precio actual: "))

pactual=calcular_precio_actualizado(aumento, precio)

print(f"El nuevo precio con el aumento es: {pactual}")