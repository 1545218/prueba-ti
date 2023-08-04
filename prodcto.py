class Producto:
    def __init__(self, nombre, marca, precio, cantidad):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.cantidad = cantidad

    def info(self):
        return f"{self.nombre} {self.marca} {self.cantidad}"

    def actaliza_catidad(self, cantidad_vendida):
        self.cantidad = self.cantidad - cantidad_vendida


