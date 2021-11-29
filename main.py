import tkinter as tk
from PIL import Image
from PIL import ImageTk
import pantalla
import tabla_funciones

root = tk.Tk()
root.title('MeQuieroMorir')
root.geometry()

def mostrar_funcion():
  if seleccionada.get() == 1:
    imagen = tabla_funciones.funcion_coseno()
  if seleccionada.get() == 2:
    imagen = tabla_funciones.funcion_rampa()
  if seleccionada.get() == 3:
    imagen = tabla_funciones.funcion_escalon()
  monitor.configure(image=imagen)
  monitor.image=imagen

seleccionada =tk.IntVar()

rb_funcion_coseno = tk.Radiobutton(root,text='Coseno',value=1,variable=seleccionada,command=mostrar_funcion)
rb_funcion_coseno.grid(row=0,column=0)

rb_rampa = tk.Radiobutton(root,text='Rampa',value=2,variable=seleccionada,command=mostrar_funcion)
rb_rampa.grid(row=0,column=1)

rb_escalon = tk.Radiobutton(root,text='Escalón',value=3,variable=seleccionada,command=mostrar_funcion)
rb_escalon.grid(row=0,column=2)

monitor = tk.Label(root,bg='black')
monitor.grid(column=0, row=1, columnspan=3)

root.mainloop()