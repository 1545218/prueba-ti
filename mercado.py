from productos import crearproductos, listarproductos

def menu():
    lista_de_productos = []
    omenu = """
    MINIMARKET
    ___________________
    1.Listar productos
    2.Agregar productos
    3.venta
    4.Salir
    """
    flag = True
    while flag:
        try:
            print(omenu)
            opcion = int(input("Elige una opcion: "))
        except ValueError:
            print('Has elegido una opcion que no esta en el menu')
        else:
            if opcion == 1:
                print("Listando productos")
                listarproductos(lista_de_productos)
            elif opcion == 2:
                print("iniciar venta")
                crearproductos(lista_de_productos)
                seleccionproducto = int(input(f'elija el numero del producto: '))
            elif opcion == 3:
                print("Agregando productos")

            elif opcion == 4:          
                print("Saliendo")
                flag = False
menu()


    


  
def ventaproductos(lista_de_productos):
    lista = []
    producto = {}
    listarproductos(lista_de_productos)

seleccionproducto = int(input('elija el numero del producto: '))
producto = listarproductos[seleccionproducto-1]
producto["cantidad"] = producto.get("cantidad") - cantidadproductos
cantidadproducto = int(input(f'escriba la cantidad de {producto.get("nombre")}:'))




    

   

   





