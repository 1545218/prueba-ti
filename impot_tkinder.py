import tkinter as tk
from tkinter import messagebox


ventana = tk.Tk()
ventana.title("Tres en Raya")


turno = "X"
tablero = [""] * 9


def verificar_ganador():
    # Combinaciones ganadoras
    combinaciones = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for comb in combinaciones:
        if tablero[comb[0]] == tablero[comb[1]] == tablero[comb[2]] != "":
            return True
    return False


def clic_casilla(casilla):
    global turno

    if tablero[casilla] == "" and not verificar_ganador():
        tablero[casilla] = turno
        botones[casilla].config(text=turno)

        if verificar_ganador():
            messagebox.showinfo("¡Ganador!", f"¡{turno} ha ganado!")
            ventana.quit()
        elif "" not in tablero:
            messagebox.showinfo("Empate", "El juego ha terminado en empate.")
            ventana.quit()
        else:
            turno = "O" if turno == "X" else "X"


botones = []
for i in range(9):
    boton = tk.Button(ventana, text="", width=10, height=3, command=lambda i=i: clic_casilla(i))
    boton.grid(row=i // 3, column=i % 3)
    botones.append(boton)

ventana.mainloop()
