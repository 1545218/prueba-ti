import tkinter as tk

def clic_tecla(tecla):
    entrada.insert(tk.END, tecla)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Incorrecto")

def eliminar():
    entrada.delete(0, tk.END)


ventana = tk.Tk()
ventana.title("Calculadora")


entrada = tk.Entry(ventana, width=40)
entrada.grid(row=0, column=0, columnspan=4)


teclas = "7894561230.+-*/"
fila = 1
columna = 0

for tecla in teclas:
    tk.Button(ventana, text=tecla, width=5, height=2, command=lambda t=tecla: clic_tecla(t)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

# Botones para calcular y borrar
tk.Button(ventana, text="=", width=5, height=2, command=calcular).grid(row=5, column=2)
tk.Button(ventana, text="C", width=5, height=2, command=eliminar).grid(row=5, column=3)


ventana.mainloop()


