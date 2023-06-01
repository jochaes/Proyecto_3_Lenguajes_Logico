from Utilitarios.PrologLink import *
from Utilitarios.MatrixGenerator import *
from Utilitarios.FileHandler import *
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

################################## Variables globales ##################################
lbIndex = 0         #Indice del Listbox 
eventT = False      #Flag para saber si se debe cambiar una palaba en el listbox
MATRIX_SIZE = 12    #Tamaño de la matriz 
listWords = []      #Lista de palabras ingresadas por el usuario

################################## Interfaz de Usuario ##################################
#*******-Panatalla Principal
window = tk.Tk()
window.title("Palabra Enredada")
window.geometry("854x500")
# window.resizable(False, False)
# window.maxsize(1024, 768)
# window.minsize(900, 675)
window.config(bg="skyblue")

################################## Funciones ##################################

#Inicia el Frame de Juego 
#En este caso el Frame de Juego es la vista que muestra:
#  -la matriz de letras al usuario 
#  - Lista de las palabras ingresadas
#  - Boton para volver al Frame de Inicio
#  - Boton para ejecutar las consulas a prolog y mostrar los resultados
def cargarGameFrame():
    time.sleep(0.2)  
    
    #Obtener la lista de palabras del usuario 
    global listWords 
    listWords = listbox.get(0, tk.END)
    
    #Validar que se haya ingresado al menos una palabra
    if len(listWords) < 1:
        msg = "Debe ingresar al menos una palabra"
        mostrarMensaje("Error", msg)
        return
    else:
        #Genera la matriz de letras
        matrix = generar_sopa_letras(MATRIX_SIZE, listWords)

        #Cargar la matriz en el frame
        print("\nCargando matriz en el frame")
        pintar_matriz(matrix, leftGameFrame)

        #Generar el conocimiento de prolog
        print ("\nGenerando conocimiento de prolog")
        conocimiento = generarHechosProlog(matrix, MATRIX_SIZE)
        
        #Guardar el conocimiento en un archivo
        print ("\nGuardando conocimiento en archivo .pl")
        storeKnowledge(conocimiento, "./Prolog/Matrix.pl")
        
        gameListbox.delete(0, tk.END)
        for palabra in listWords:
            gameListbox.insert(tk.END, palabra)
        
        startFrame.pack_forget()  # Ocultar frame_a
        gameFrame.pack(expand=True, fill=tk.BOTH)  # Mostrar frame_b
        window.update_idletasks()
    
    
#Inicia el Frame de Inicio
def cargarStartFrame():
    time.sleep(0.2)
    gameFrame.pack_forget()  # Ocultar frame_b
    startFrame.pack(expand=True, fill=tk.BOTH)  # Mostrar frame_a
    window.update_idletasks()
    
    
#Muestra notificaciones al usuario
def mostrarMensaje(title, message):
        self = window
        top = tk.Toplevel(self)
        top.details_expanded = False
        top.title(title)
        
        top.geometry(f"{window.winfo_width()}x100+{'{}'}+{'{}'}".format(self.winfo_x(), self.winfo_y()))
        top.resizable(False, False)
        top.rowconfigure(0, weight=0)
        top.rowconfigure(1, weight=1)
        top.columnconfigure(0, weight=1)
        top.columnconfigure(1, weight=1)
        tk.Label(top, image="::tk::icons::question").grid(row=0, column=0, pady=(7, 0), padx=(7, 7), sticky="e")
        tk.Label(top, text=message).grid(row=0, column=1, columnspan=2, pady=(7, 7), sticky="w")
        tk.Button(top, text="OK", command=top.destroy).grid(row=1, column=0,ipadx=100, columnspan=2,  sticky="n")
        

    

################################## Start Frame ##################################

#*******- Funciones de Panatalla de Inicio de la Aplicacion

#Verifica y añade las palabras ingresadas por el usuario al componente de ListBox
def anadirPalabra(self, event=None):
    global lbIndex
    global eventT
    inputWord = entry.get()

    if len(inputWord) > MATRIX_SIZE:
        msg = f"La palabra no puede ser mayor a {MATRIX_SIZE} letras"
        mostrarMensaje("Error", msg)
        return

    entry.delete(0, tk.END)
    if eventT == True:
        if inputWord == '':
            listbox.delete(lbIndex)
        else:
            listbox.insert(lbIndex, inputWord)
            listbox.delete(lbIndex + 1)
            eventT = False
    else:
        if inputWord != '':   
            listbox.insert(tk.END, inputWord)
            print(inputWord)


# Cuando el Usuario selecciona una palabra de la lista, se activa el evento onselect
# para cargar la palabra en el Entry y poder cambiarla o eliminarla(Si borra toda la palabra).
def onSelect(evt):
    global lbIndex
    global eventT
    w = evt.widget
    entry.delete(0, tk.END)
    if w.curselection().__len__() > 0:
        lbIndex = w.curselection()[0]
        eventT = True
        value = w.get(lbIndex)
        entry.insert(0, value)
        print('You selected item %d: "%s"' % (lbIndex, value))
    
#*******- Pantalla de Inicio de la Aplicacion
#Ventana de Incio 
startFrame = tk.Frame(window, bg="white")
startFrame.pack(expand=True, fill=tk.BOTH)
# startFrame.grid(row=0, column=0, padx=1, pady=1)

# Label para el Titulo del Juego
gameTitle_label = tk.Label(startFrame, text="Bienvenido a Palabra Enredada", font=("Arial", 20),bg="white", fg="black")
gameTitle_label.pack(padx=10, pady=5)
# gameTitle_label.grid(row=0, column=0, padx=10, pady=5)

inputWord_label = tk.Label(startFrame, text="Ingrese las palabras:", bg="white", fg="black")  
inputWord_label.pack(padx=10, pady=5) 
# inputWord_label.grid(row=1, column=0, padx=10, pady=5)

# Input para ingresar las palabras
entry = tk.Entry(startFrame,bg="white", fg="black")
entry.pack(padx=10, pady=5) 
#Cuando se presiona enter
entry.bind("<Return>", anadirPalabra)

#ListBox para mostrar las palabras ingresadas
listFrame = tk.Frame(startFrame, bg="white")
listFrame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
listScroll = tk.Scrollbar(listFrame, orient=tk.VERTICAL)
listbox = tk.Listbox(listFrame, width=50, height=10, yscrollcommand=listScroll.set, bg="white", fg="black")
listScroll.config(command=listbox.yview)
listScroll.pack(padx=10, pady=5, side=tk.RIGHT, fill=tk.Y) 
listbox.pack(padx=10, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True) 
# listScroll.grid(row=3, column=1, sticky=tk.N+tk.S)
# listbox.grid(row=3, column=0, padx=10, pady=5)
listbox.bind('<<ListboxSelect>>', onSelect)


# Boton para cargar la ventana del juego
button_a = tk.Button(startFrame, text="Iniciar Palabras Enredadas", command=cargarGameFrame, bg="white", fg="black")
button_a.pack(padx=10, pady=5)
# button_a.grid(row=4, column=0, padx=10, pady=5)



################################## Game Frame ##################################

#*******- Pantalla del Juego

gameFrame = tk.Frame(window, bg="lightblue")
gameFrame.pack(expand=True, fill=tk.BOTH)


#Frame superior 
topGameFrame = tk.Frame(gameFrame, bg="brown")
topGameFrame.pack(fill=tk.X, side=tk.TOP, anchor=tk.N)

gameTitle3_Label = tk.Label(topGameFrame, text="Bienvenido a Palabra Enredada", font=("Arial", 20),bg="white", fg="black")
gameTitle3_Label.pack(expand=True, fill=tk.Y, side=tk.RIGHT, anchor=tk.N)

goBack_btn = tk.Button(topGameFrame, text="Mostrar Ventana A", command=cargarStartFrame)
goBack_btn.pack(expand=True, fill=tk.Y, side=tk.LEFT, anchor=tk.N)

#Frame inferior
bottomGameFrame = tk.Frame(gameFrame, bg="green")
bottomGameFrame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, anchor=tk.N)

#Frame izquierdo
leftGameFrame = tk.Frame(bottomGameFrame, bg="yellow")
leftGameFrame.pack(expand=False, fill=tk.BOTH, side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

#Frame derecho
rightGameFrame = tk.Frame(bottomGameFrame, bg="pink")
rightGameFrame.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT, anchor=tk.N,padx=10, pady=10)

#ListBox para mostrar las palabras ingresadas
gameListFrame = tk.Frame(rightGameFrame, bg="white")
gameListFrame.pack(fill=tk.BOTH, expand=True)
gameListScroll = tk.Scrollbar(gameListFrame, orient=tk.VERTICAL)
gameListbox = tk.Listbox(gameListFrame, width=1, yscrollcommand=gameListScroll.set, bg="white", fg="black")
gameListScroll.config(command=listbox.yview)
gameListScroll.pack(side=tk.RIGHT, fill=tk.Y) 
gameListbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 


#Funcion para cambiar el color de las etiquetas
#Muestra la soucion en pantalla de las palabras encontradas por prolog
#Pinta en Verde las palabras que sólo se encontraron una vez
#Pinta en Fucsia las palabras que tienen más de una ruta 
def cambiarColor(contenedor, resultados):
    
    #Si solo hay un camino lo pinta de verde, 
    #si hay mas de uno lo pinta de fucsia
    if len(resultados) == 1:
        color = "green"
    else:
        color = "purple"

    for posiciones in resultados:
    
        for posicion in posiciones:

            x = posicion[0]
            y = posicion[1]
            etiqueta = contenedor.grid_slaves(row=x, column=y)[0]
            etiqueta.config(bg=color)

#Funcion para consultar las palabras en prolog
def solucion():
    print ("\nBuscando palabras en la matriz de letras")
    for palabra in listWords:
        print(palabra)
        resultado = consultarPalabra(palabra)        #Consulta la Palabra en Prolog
        cambiarColor(leftGameFrame, resultado)       #Cambiar el color de la respuesta que da prolog
        print(resultado)
        print("\n")

#Boton para encontrar las palabras con prolos 
solve_btn = tk.Button(rightGameFrame, text="Solucionar", command=solucion)
solve_btn.pack(expand=False, fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S)

#Dibuja la matriz generada por python 
def pintar_matriz(matriz, contenedor):
    
    print(window.winfo_width())
    print(window.winfo_height())
    padx = ( (window.winfo_width() * 0.75) // len(matriz) // 3 )
    pady = (padx * 0.60)
    print(padx)
    print(pady)

    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            etiqueta = tk.Label(contenedor, text=str(elemento),padx=padx, pady=pady, bg="white", fg="black", border=1, relief="solid")
            etiqueta.grid(row=i, column=j, columnspan=1, rowspan=1, sticky="nsew")



'''
#Generación de la Matriz de Letras
tamano = 10
palabras = ['hola', 'mundo', 'adios', 'ropa', 'casa','camion']
matrizPalabrasEnredadas = generar_sopa_letras(tamano, palabras)

print("Matriz de Letras")
# Imprimir la sopa de letras generada
for fila in matrizPalabrasEnredadas:
    print(' '.join(fila))


#Generación del conocimeinto de la Matriz de Letras
conocimiento = prologFactsGenerator(matrizPalabrasEnredadas, tamano)
print ("\nConocimiento")
for elemento in conocimiento:
    print(elemento)

#Guarda el conocimiento en un archivo .pl
print ("\nGuardando conocimiento en archivo .pl")
storeKnowledge(conocimiento, "./Prolog/Matrix.pl")

#Busca las palabras en la matriz de letras
print ("\nBuscando palabras en la matriz de letras")
for palabra in palabras:
    print(palabra)
    resultado = wordPath(palabra)
    print(resultado)
    print("\n")


'''

data = [
    ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "5", "6"],
    ["u", "v", "w", "x", "y", "z", "ñ", "á", "é", "í", "5", "6"],
    ["ó", "ú", "ü", "0", "1", "2", "3", "4", "5", "6", "5", "6"],
    ["7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "5", "6"],
    ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "5", "6"],
    ["r", "s", "t", "u", "v", "w", "x", "y", "z", "ñ", "5", "6"],
    ["á", "é", "í", "ó", "ú", "ü", "0", "1", "2", "3", "5", "6"],
    ["4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "5", "6"],
    ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "5", "6"],
    ["h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "5", "6"],
    ["r", "s", "t", "u", "v", "w", "x", "y", "z", "ñ", "5", "6"],
    ["á", "é", "í", "ó", "ú", "ü", "0", "1", "2", "3", "5", "6"]
]



cargarStartFrame()

# pintar_matriz(data, leftGameFrame)
# cambiarColor(leftGameFrame, 0, 0, "red")

window.mainloop()