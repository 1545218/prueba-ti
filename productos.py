def creaproductos(lista_productos):
    flag=True
    while flag:
        try:
            nombreproducto = input("nombre del producto: ")
            marcaproducto = input("maraca del producto: ")
            costoproducto = int(input("costo del producto: "))
            cantidaproducto = int(input("cantidad del producto: "))
        except ValueError:
            print("algo salio mal intentalo otra vez")
        else:
            producto["nombre"]= nombreproducto
            producto["marca"]= marcaproducto
            producto["costo"]= costoproducto
            producto["cantidad"]= cantidaproducto
            lista_productos.append(producto)
            producto = {}
            pregunta = input("desea agrear mas productos? si/no")
            if str(pregunta) != "si":
               flag = False

               print(lista_productos)


#producto

print("""
      supermercado
      elija la opcion
1. listar los productos
2. agregar mas productos
3. hacer la venta
    """  )

def listaproductos(lista_productos):
    for producto in lista_productos:
        print(f"{producto.get('nombre')} | {producto.get('cantidad')} | {producto.get('costo')}")
    

    