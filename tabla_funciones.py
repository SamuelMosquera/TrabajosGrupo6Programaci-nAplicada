import numpy as np
import pantalla

RESOLUCION = 512
NUMERO_DATOS = 1024

def funcion_coseno():

    frame = np.zeros((RESOLUCION, NUMERO_DATOS,3), dtype=np.uint8)
    print(frame.shape,frame.dtype)

    for i in range(NUMERO_DATOS):
        frame[511-int(255*np.cos(i/163)+255),i,:] = np.array([255,255,255])

    return pantalla.crear_imagen(frame)
 

def funcion_rampa():

    frame = np.zeros((RESOLUCION, NUMERO_DATOS,3), dtype=np.uint8)
    print(frame.shape,frame.dtype)

    for i in range(RESOLUCION):
        frame[(RESOLUCION-i)-1,2*i,:] = np.array([255,255,255])

    return pantalla.crear_imagen(frame)

def funcion_escalon():

    frame = np.zeros((RESOLUCION, NUMERO_DATOS,3), dtype=np.uint8)
    print(frame.shape,frame.dtype)

    for i in range(int(NUMERO_DATOS/2)):
        frame[RESOLUCION-1,i,:] = np.array([255,255,255])
    
    for i in range(RESOLUCION):
        frame[i,int(NUMERO_DATOS/2),:] = np.array([255,255,255])
    
    for i in range(int(NUMERO_DATOS/2),NUMERO_DATOS):
        frame[0,i,:] = np.array([255,255,255])
        

    return pantalla.crear_imagen(frame)