
    
import tkinter as tk
from urllib.request import urlopen  
from PIL import Image, ImageTk  
from io import BytesIO

def descargarPortada():

    urlImagen ="https://github.com/maximoivk78/proyecto/blob/main/graficacion.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargarFondo():

    urlImagen ="https://github.com/maximoivk78/proyecto/blob/main/3.png?raw=true"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def mostrarOpcion1():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 1", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion2():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 2", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)


        
def mostrarOpcion3():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 1", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def mostrarOpcion4():
    limpiarVentana()
    label = tk.Label(ventana, text="Elegiste la Opción 2", font=("Arial", 16))
    label.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

def limpiarVentana():  
    
    for widget in ventana.winfo_children():  
     
        widget.destroy()

        

        
def mostrarMenu():
    limpiarVentana()

    #Coloco el fondo
    etiqueta = tk.Label(ventana, image=ventana.fondo)
    etiqueta.place(width=ancho, height=alto)
    
    label = tk.Label(ventana, text="Menú Principal", font=("Arial", 18, "bold"))
    label.pack(pady=20)

    boton1 = tk.Button(ventana, text="Opción 1", font=("Arial", 14), width=20, command=mostrarOpcion1)
    boton1.place(x=700, y=1000)

    boton2 = tk.Button(ventana, text="Opción 2", font=("Arial", 14), width=20, command=mostrarOpcion2)
    boton1.place(x=700, y=1100)

    boton3 = tk.Button(ventana, text="Opción 3", font=("Arial", 14), width=20, command=mostrarOpcion3)
    boton3.pack(pady=10)

    boton4 = tk.Button(ventana, text="Opción 4", font=("Arial", 14), width=20, command=mostrarOpcion4)
    boton4.pack(pady=10)


def main():
    global ventana
    ventana = tk.Tk()
    ventana.title("Imagen en Tkinter")


    ancho = ventana.winfo_screenwidth()
     
    alto = ventana.winfo_screenheight()
     
    ventana.geometry(f"{ancho}x{alto}")

    
    #Portada
    imagen=descargarPortada()
    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    portada = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.portada=portada

    #Fondo
    imagen=descargarFondo()
    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondo = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.fondo=fondo


    #Coloco portada
    etiqueta = tk.Label(ventana, image=ventana.portada)
    etiqueta.place(width=ancho, height=alto)


    
    boton1 = tk.Button(ventana, text="Comenzar", command=mostrarMenu)
    boton1.place(x=700, y=600)
    



    ventana.mainloop()  
if __name__=="__main__":
    main()
