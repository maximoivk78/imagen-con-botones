import tkinter as tk  
from urllib.request import urlopen  
from PIL import Image, ImageTk  
from io import BytesIO

def descargarFondo():

    urlImagen ="https://github.com/maximoivk78/proyecto/blob/main/graficacion.png"
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


      ventana.mainloop()  
if __name__=="__main__":
    main()
