from PIL import Image, ImageTk

def crear_imagen(funcion):
  im=Image.fromarray(funcion)
  img=ImageTk.PhotoImage(image=im)
  return img