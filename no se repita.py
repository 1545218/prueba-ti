# Ejemplo utilizando un diccionario
productos = {}

while True:
    producto = input("Ingrese el nombre del producto (o 'salir' para terminar): ")
    if producto.lower() == 'salir':
        break

    if producto not in productos:
        productos[producto] = 1
        print(f"Producto '{producto}' agregado correctamente.")
    else:
        print(f"El producto '{producto}' ya existe en la lista y no será agregado.")

lista_productos = list(productos.keys())
print("Lista de productos sin repeticiones:", lista_productos)
