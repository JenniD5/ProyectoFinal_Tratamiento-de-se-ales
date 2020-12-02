import pyaudio 
import numpy as np
import wave
from tkinter import *

ventana = Tk()
ventana.title("Analisis")
ventana.configure(bg='beige')

ventana.geometry("350x300")

#formato de audio de microfono
PROFUNDIDAD_BITS = pyaudio.paInt16
CANALES = 1
FRECUENCIA_MUESTREO = 44100

#tamaño de chunk
CHUNK = 2048

SEGUNDOS_GRABACION = 1


freqActual = StringVar()
strCuerda = StringVar()
strAfinacion = StringVar()





window = np.blackman(CHUNK)
def hola():
    
    def analizar(stream):
        data = stream.read(CHUNK, exception_on_overflow=False)
        #"2048h"
        waveData = wave.struct.unpack("%dh"%(CHUNK), data)
        npData=np.array(waveData)

        dataEntrada = npData * window
        fftData = np.abs(np.fft.rfft(dataEntrada))

        indiceFrecuenciaDominante = fftData[1:].argmax() + 1
        
        #cambio de indice  Hz
        y0,y1,y2 = np.log(fftData[indiceFrecuenciaDominante-1: indiceFrecuenciaDominante+2])
        x1 =(y2 - y0) * 0.5/(2 * y1 -y2 - y0)
        frecuenciaDominante = (indiceFrecuenciaDominante + x1)* FRECUENCIA_MUESTREO/CHUNK
        frecuencia = str(frecuenciaDominante)
        print ("frecuencia dominante: "+ str(frecuenciaDominante) + "Hz", end='\r')
        freqActual.set(frecuencia)
        
        
        tolerancia=13
        toleranciaAfinacion = 1.3

        if frecuenciaDominante > 82.4 - tolerancia and frecuenciaDominante < 82.4 + tolerancia:
            Cuerda= "6ta Mi con una frecuencia de 82.4 Hz"
            if frecuenciaDominante >82.4 - toleranciaAfinacion and frecuenciaDominante < 82.4 + toleranciaAfinacion:
                Afinacion = "la afinacion es la correcta"
            elif frecuenciaDominante < 82.4 + toleranciaAfinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frecuenciaDominante > 110.0 - tolerancia and frecuenciaDominante < 110.0 + tolerancia:
            Cuerda= "5ta La con una frecuencia de 110.0 Hz"
            if frecuenciaDominante >110.0 - toleranciaAfinacion and frecuenciaDominante < 110.0 + toleranciaAfinacion:
                Afinacion = "la afinacion es correcta"
            elif frecuenciaDominante < 110.0 + toleranciaAfinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frecuenciaDominante > 146.83 - tolerancia and frecuenciaDominante < 146.83 + tolerancia:
            Cuerda= "4ta Re con una frecuencia de 146.83 Hz"
            if frecuenciaDominante >146.83 - toleranciaAfinacion and frecuenciaDominante < 146.83 + toleranciaAfinacion:
                Afinacion = "la afinacion es la correcta"
            elif frecuenciaDominante < 146.83 + toleranciaAfinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frecuenciaDominante > 196.0 - tolerancia and frecuenciaDominante < 196.0 + tolerancia:
            Cuerda= "3ra Sol con una frecuencia de 196.0 Hz"
            if frecuenciaDominante >196.0 - toleranciaAfinacion and frecuenciaDominante < 196.0 + toleranciaAfinacion:
                Afinacion = "la afinacion es la correcta"
            elif frecuenciaDominante < 196.0 + toleranciaAfinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"
        
        elif frecuenciaDominante > 246.94- tolerancia and frecuenciaDominante < 246.94 + tolerancia:
            Cuerda= "2da Si con una frecuencia de 246.94 Hz"
            if frecuenciaDominante >246.94 - toleranciaAfinacion and frecuenciaDominante < 246.94 + toleranciaAfinacion:
                Afinacion = "la afinacion es la correcta"
            elif frecuenciaDominante < 246.94 + toleranciaAfinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"

        elif frecuenciaDominante > 329.63 - tolerancia and frecuenciaDominante < 329.63  + tolerancia:
            Cuerda= "1ra Mi con una frecuencia de  329.63 Hz"
            if frecuenciaDominante >329.63  - toleranciaAfinacion and frecuenciaDominante < 329.63  + toleranciaAfinacion:
                Afinacion = "la afinacion es la correcta"
            elif frecuenciaDominante < 329.63  + toleranciaAfinacion:
                Afinacion = "debe apretar la cuerda "
            else:
                Afinacion = "debe aflojar la cuerda"
        else:
            Cuerda = "la cuerda no ha identificada"
            Afinacion = "presione de nuevo el boton de ingresar"
        

        strCuerda.set(Cuerda)
        #freqActual.set(freqActual)
        strAfinacion.set(Afinacion)


        


    
    if __name__=="__main__":
   
        p = pyaudio.PyAudio()
        stream = p.open(format=PROFUNDIDAD_BITS, channels=CANALES, rate=FRECUENCIA_MUESTREO, input=True, frames_per_buffer=CHUNK)
        
        for i in range(0, int(FRECUENCIA_MUESTREO * SEGUNDOS_GRABACION / CHUNK)):
            analizar(stream)
            #etiqueta1.after(1000,hola)
            


        #etiqueta1.after(1000,hola)
        stream.stop_stream()
        stream.close()
        p.terminate()
    

boton = Button(ventana, text="Ingresar", command=hola, background="pink")
boton.pack(pady=21)

etiquetaCuerda = Label(ventana, textvariable=strCuerda, background="beige")
etiquetaCuerda.pack()

etiqueta1=Label(ventana, textvariable=freqActual, background="beige")
etiqueta1.pack()

etiquetaAfinacion = Label(ventana, textvariable=strAfinacion, background="beige")
etiquetaAfinacion.pack()


ventana.mainloop()  
   

 




   
