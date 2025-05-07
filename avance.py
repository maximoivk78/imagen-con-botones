
    
import tkinter as tk
from urllib.request import urlopen  
from PIL import Image, ImageTk  
from io import BytesIO

def descargarFondo():

    urlImagen ="https://github.com/maximoivk78/proyecto/blob/main/graficacion.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen
def main():
    
    ventana = tk.Tk()
    ventana.title("Imagen en Tkinter")


   
    ancho = ventana.winfo_screenwidth()
     
    alto = ventana.winfo_screenheight()
     
    ventana.geometry(f"{ancho}x{alto}")

    imagen=descargarFondo()

    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)

   
    imagenTk = ImageTk.PhotoImage(imagenRedimensionada)

   

    etiqueta = tk.Label(ventana, image=imagenTk)
    etiqueta.pack()  

    boton1 = tk.Button(ventana, text="Opcion 1", command=accionOpcion1)
    boton1.pack(pady=5)
    
    boton2 = tk.Button(ventana, text="Opcion 2", command=accionOpcion2)
    boton2.pack(pady=5)
    
    boton3 = tk.Button(ventana, text="Opcion 3", command=accionOpcion3)
    boton3.pack(pady=5)
    
    boton4 = tk.Button(ventana, text="Opcion 4", command=accionOpcion4)
    boton4.pack(pady=5)


    ventana.mainloop()  
if __name__=="__main__":
    main()
