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

def descargarbalatro():

    urlImagen ="https://static.wikia.nocookie.net/balatrogame/images/e/ef/Joker.png/revision/latest?cb=20230925003651"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen

def descargardeltarune():

    urlImagen ="https://static.wikia.nocookie.net/delta-rune/images/a/ad/Ralsei_yeah.png/revision/latest?cb=20211016211545&path-prefix=es"
    datosImagen = urlopen(urlImagen)  
    imagenBinaria = datosImagen.read()  
    
    imagen = Image.open(BytesIO(imagenBinaria))
    return imagen



def limpiarVentana():  
    
    for widget in ventana.winfo_children():  
     
        widget.destroy()
        
    
        

        
def mostrarMenu():
    limpiarVentana() 
    #Coloco fondo
    etiqueta = tk.Label(ventana, image=ventana.fondo).place(width=ancho, height=alto)
    etiqueta = tk.Label(ventana, text="¿cúal es tu videojuego preferencial?", font=("Comic Sans MS", 32))
    etiqueta.pack()
    
    
    
    boton2 = tk.Button(ventana, text="Balatro", font=("Arial", 14), width=20, command=menu2)
    boton2.place(x=560, y=100)

    boton3 = tk.Button(ventana, text="deltarune", font=("Arial", 14), width=20, command=menu3)
    boton3.place(x=560, y=200)

    
    
def menu2():
   
    limpiarVentana()
    #Coloco fondo
    
    
    
    etiqueta = tk.Label(ventana, image=ventana.fondo).place(width=ancho, height=alto)

  
    
    etiqueta = tk.Label(ventana, text="balatro", font=("Comic Sans MS", 64))
    etiqueta.pack()
    
    
    
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)

    etiqueta = tk.Label(ventana, image=ventana.balatro).place(x=625, y=400, width=200, height=200)
    
def menu3():
   
    limpiarVentana()
    #Coloco fondo
    etiqueta = tk.Label(ventana, image=ventana.fondo).place(width=ancho, height=alto)
    
    etiqueta = tk.Label(ventana, text="deltarune", font=("Comic Sans MS", 64))
    etiqueta.pack()
    
    boton_volver = tk.Button(ventana, text="Volver", font=("Arial", 12), command=mostrarMenu)
    boton_volver.pack(pady=10)
    
    etiqueta = tk.Label(ventana, image=ventana.deltarune).place(x=625, y=400, width=200, height=200)
    
def main():
    global ventana
    global ancho
    global alto
    
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


    #Coloco portada
    etiqueta = tk.Label(ventana, image=ventana.portada)
    etiqueta.place(width=ancho, height=alto)


    
    boton1 = tk.Button(ventana, text="Comenzar", command=mostrarMenu)
    boton1.place(x=700, y=600)
    
    
    imagen = descargarFondo()
    imagenRedimensionada = imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
    fondo = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.fondo = fondo

    imagen = descargarbalatro()
    imagenRedimensionada = imagen.resize((200, 200), Image.Resampling.LANCZOS)
    balatro = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.balatro = balatro
    
    imagen = descargardeltarune()
    imagenRedimensionada = imagen.resize((200, 200), Image.Resampling.LANCZOS)
    deltarune = ImageTk.PhotoImage(imagenRedimensionada)
    ventana.deltarune = deltarune
    
   
    ventana.mainloop()  
if __name__=="__main__":
    main()
