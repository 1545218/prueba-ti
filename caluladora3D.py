import numpy as np

def sumar_vectores(a, b):
    return np.add(a, b)

def restar_vectores(a, b):
    return np.subtract(a, b)

def multiplicar_vectores(a, b):
    return np.multiply(a, b)

def dividir_vectores(a, b):
    return np.divide(a, b)

def obtener_vector():
    a = float(input("Ingrese la coordenada a: "))
    b = float(input("Ingrese la coordenada b: "))
    c = float(input("Ingrese la coordenada c: "))
    d = float(input("Ingrese la coordenada d: "))
    return np.array([a, b, c, d])

def main():
    print("Calculadora 3D")
    print("1. Sumar vectores")
    print("2. Restar vectores")
    print("3. Multiplicar vectores")
    print("4. Dividir vectores")

    opcion = int(input("Seleccione una opción (1, 2, 3 o 4): "))

    if opcion == 1:
        vector1 = obtener_vector()
        vector2 = obtener_vector()
        resultado = sumar_vectores(vector1, vector2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        vector1 = obtener_vector()
        vector2 = obtener_vector()
        resultado = restar_vectores(vector1, vector2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        vector1 = obtener_vector()
        vector2 = obtener_vector()
        resultado = multiplicar_vectores(vector1, vector2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        vector1 = obtener_vector()
        vector2 = obtener_vector()
        resultado = dividir_vectores(vector1, vector2)
        print("El resultado de la división es:", resultado)
    else:
        print("Opción no válida. Por favor, seleccione 1, 2, 3 o 4.")

if __name__ == "__main__":
    main()
