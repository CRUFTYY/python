#Importamos las librerias
import tkinter as tk
from tkinter import font
import datetime

#Definimos el reloj
def time():
    string = datetime.datetime.now().strftime("%H:%M:%S %p")
    lbl.config(text = string)
    lbl.after(1000, time)

root = tk.Tk()
root.title("Reloj CRUFTY")

#Pantalla completa al abrir
def exit_fullscreen():
    root.attributes("-fullscreen", False)
exit_button = tk.Button(root, text="Salir de la pantalla completa", command=exit_fullscreen)
exit_button.pack()
#fin

#root.state("zoomed")    -esta linea sirve para que se esté en  pantalla completa pero puedas achicar, minimizar y cerrar la ventana 

#Proporciones y colores
fnt = font.Font(family='Helvetica', size=60, weight='bold')
lbl = tk.Label(root, font=fnt, background = 'purple', foreground = 'black')
lbl.place(relx=0.5, rely=0.5, anchor='center')
time()
root.geometry("400x400")
#fin

#Cierrre del loop
root.mainloop()
#fin