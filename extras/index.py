from tkinter import *

ventana = Tk()
ventana.title("Analisi")

ventana.geometry("350x300")

def ingresar():
    etiquetafreqcaptadacuerda = Label(ventana, text="cuerda mas cercana a la frecuencia captada")
    etiquetafreqcaptadacuerda.pack(pady=15)
    etiquetafreqdeseada = Label(ventana,text="frecuencia que debe tener")
    etiquetafreqdeseada.pack(pady=15)
    etiquetafreqactual = Label(ventana, text="frecuencia actual")
    etiquetafreqactual.pack(pady=15)
    etiquetApreparAflojar = Label(ventana,text="apretar o aflojar")
    etiquetApreparAflojar.pack(pady=15)
   
  

boton = Button(ventana, text="ingresar", command=ingresar)
boton.pack(pady=21)

ventana.mainloop()