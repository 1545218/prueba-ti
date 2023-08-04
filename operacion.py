from prodcto import Producto


lista_producto = []
p = Producto("lpatop", "asus", 2000, 5)
#lista_producto.append(p)
#print(lista_producto)
#producto = lista_producto[0]
#print(producto.info())

nombre_p= input("nombre del producto: ")
marca_p = input("marca del producto: ")
precio_P = input("precio del producto:")
cantidad_p = input("cantida del producto:")
t = Producto(nombre_p, marca_p, precio_P, cantidad_p,)
print(t.info())