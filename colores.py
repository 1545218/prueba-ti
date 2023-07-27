import random

def adivina_color():
    colores = ["amarillo", "rojo", "azul"]
    color_secreto = random.choice(colores)
    intentos = 0

    while True:
        intentos += 1
        color_usuario = input("Adivina el color (amarillo, rojo, azul): ").lower()

        if color_usuario == color_secreto:
            print("¡Correcto! Adivinaste el color en", intentos, "intentos.")
            break
        else:
            print("Intenta de nuevo. El color no es correcto.")

adivina_color()
