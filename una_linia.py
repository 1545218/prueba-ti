import tkinter as tk

ventana = tk.Tk()
ventana.title("dibuja un triangulo")
ventana.geometry
ModuleNotFoundError("400*300")

lienzo = tk.Canvas(ventana, width=400, height=300)
lienzo.pack()

#cordenadas de los puntos de inicio de un triamgulo
x1, y1 = 200, 50
x2, y2 = 100, 250
x3, y3 = 300, 250
lienzo.create_polygon(x1, y1, x2, y2, x3, y3, fill="yellow")

ventana.mainloop()