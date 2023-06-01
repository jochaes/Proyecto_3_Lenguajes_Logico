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

#Variables para saber si se han cargado los datos
loadedMatrix = False
loadedWords = False

emptyMatrix = [['0' for _ in range(MATRIX_SIZE)] for _ in range(MATRIX_SIZE)] #Matriz vacia


################################## Interfaz de Usuario ##################################
#*******-Panatalla Principal
window = tk.Tk()
window.title("Palabra Enredada")
window.geometry("854x510")
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
    
    # #Obtener la lista de palabras del usuario 
    # global listWords 
    # listWords = listbox.get(0, tk.END)
    
    # #Validar que se haya ingresado al menos una palabra
    # if len(listWords) < 1:
    #     msg = "Debe ingresar al menos una palabra"
    #     mostrarMensaje("Error", msg)
    #     return
    # else:
    #     #Genera la matriz de letras
    #     matrix = generar_sopa_letras(MATRIX_SIZE, listWords)

    #Cargar la matriz en el frame
    print("\nCargando matriz en el frame")
    pintar_matriz(emptyMatrix, leftGameFrame)

    #     #Generar el conocimiento de prolog
    #     print ("\nGenerando conocimiento de prolog")
    #     conocimiento = generarHechosProlog(matrix, MATRIX_SIZE)
        
    #     #Guardar el conocimiento en un archivo
    #     print ("\nGuardando conocimiento en archivo .pl")
    #     storeKnowledge(conocimiento, "./Prolog/Matrix.pl")
        
    #     gameListbox.delete(0, tk.END)
    #     for palabra in listWords:
    #         gameListbox.insert(tk.END, palabra)
        
    gameFrame.pack(expand=True, fill=tk.BOTH)  # Mostrar frame_b
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

#Carga el filechooser para elegir el archivo json
def seleccionarArchivo():
    
    filetypes = (
        ('text files', '*.json'),
        ('All files', '*.json')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='./',
        filetypes=filetypes)
    
    return filename
    
#Carga la Matriz de letras
def cargarMatriz():
    print("Cargando matriz")
    filename = seleccionarArchivo()
    if(filename != ""):
        matrix = getInputDataFromJson(filename,"matriz")

        if(matrix != None):

            if(len(matrix) != len(matrix[0])):
                mostrarMensaje("Error", "La matriz debe ser Cuadrada")
                return
            
            global MATRIX_SIZE
            MATRIX_SIZE = len(matrix)

            print ("\nGenerando conocimiento de prolog")
            conocimiento = generarHechosProlog(matrix, MATRIX_SIZE)
            print ("\nGuardando conocimiento en archivo .pl")
            storeKnowledge(conocimiento, "./Prolog/Matrix.pl")
            print("\nCargando matriz en el frame")
            pintar_matriz(matrix, leftGameFrame)
            global loadedMatrix
            loadedMatrix = True
        else:
            mostrarMensaje("Error", "No se pudo cargar la matriz, \n Verifique que el json tenga el atributo \"matriz\"")
    else:
        print("No se selecciono ningun archivo")
    

#Carga la lista de palabras
def cargarPalabras():
    print("Cargando palabras")    
    filename = seleccionarArchivo()
    if(filename != ""): 
        palabras = getInputDataFromJson(filename,"palabras")
        
        if(palabras != None):
            global listWords 
            listWords = palabras
            print("Cargando palabras en listbox")
            gameListbox.delete(0, tk.END)
            for palabra in listWords:
                gameListbox.insert(tk.END, palabra)
            global loadedWords
            loadedWords = True

        else:
            mostrarMensaje("Error", "No se pudo cargar la lista de palabras, \n Verifique que el json tenga el atributo \"palabras\"")
        
    else:
        print("No se selecciono ningun archivo")    



################################## Game Frame ##################################


#*******- Funciones del Juego
'''
    Funcion para cambiar el color de las etiquetas
    Muestra la soucion en pantalla de las palabras encontradas por prolog
    Pinta en Verde las palabras que sólo se encontraron una vez
    Pinta en Fucsia las palabras que tienen más de una ruta 
'''
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
            etiqueta.config(bg=color, fg="white")
            

#Funcion para consultar las palabras en prolog
def solucion():
    print ("\nBuscando palabras en la matriz de letras")

    if ( (loadedMatrix == True) and (loadedWords == True)):
        for palabra in listWords:
            print(palabra)
            
            resultado = consultarPalabra(palabra.lower())        #Consulta la Palabra en Prolog
            cambiarColor(leftGameFrame, resultado)       #Cambiar el color de la respuesta que da prolog
            print(resultado)
            print("\n")
    else:
        mostrarMensaje("Error", "No se ha cargado la matriz o las palabras")



#Dibuja la matriz generada por python 
def pintar_matriz(matriz, contenedor):
    
    for widget in contenedor.winfo_children():
        widget.destroy()


    print(window.winfo_width())
    print(window.winfo_height())
    padx = ( (window.winfo_width() * 0.75) // len(matriz) // 3 )
    pady = (padx * 0.60)
    print(padx)
    print(pady)

    for i, fila in enumerate(matriz):
        for j, elemento in enumerate(fila):
            etiqueta = tk.Label(contenedor, text=str(elemento),padx=padx, pady=pady, bg="#DAF7DC", fg="black", border=1, relief="solid")
            etiqueta.grid(row=i, column=j, columnspan=1, rowspan=1, sticky="nsew")



#*******- Pantalla del Juego

gameFrame = tk.Frame(window, bg='#2F4858')
gameFrame.pack(expand=True, fill=tk.BOTH)

#Frame superior 
topGameFrame = tk.Frame(gameFrame, bg='#336699')
topGameFrame.pack(fill=tk.X, side=tk.TOP, anchor=tk.N, ipadx=2, ipady=2)

gameTitle3_Label = tk.Label(topGameFrame, text="Bienvenido a Palabra Enredada", font=("Arial", 20),bg="#336699", fg="#86BBD8")
gameTitle3_Label.pack(expand=True, fill=tk.Y, side=tk.LEFT, anchor=tk.N)

loadMatrixBtn = tk.Button(topGameFrame, text="Cargar Palabras", command=cargarPalabras, bg="#9EE493", fg="#2F4858" )
loadMatrixBtn.pack(expand=True, fill=tk.Y, side=tk.RIGHT, anchor=tk.N)

loadWordsBtn = tk.Button(topGameFrame, text="Cargar Matriz", command=cargarMatriz,bg="#9EE493", fg="#2F4858")
loadWordsBtn.pack(expand=True, fill=tk.Y, side=tk.RIGHT, anchor=tk.N)

#Frame inferior
bottomGameFrame = tk.Frame(gameFrame, bg="#2F4858")
bottomGameFrame.pack(expand=True, fill=tk.BOTH, side=tk.TOP, anchor=tk.N)

#Frame izquierdo
leftGameFrame = tk.Frame(bottomGameFrame, bg="#2F4858")
leftGameFrame.pack(expand=False, fill=tk.BOTH, side=tk.LEFT, anchor=tk.N, padx=10, pady=10)

#Frame derecho
rightGameFrame = tk.Frame(bottomGameFrame, bg="#2F4858")
rightGameFrame.pack(expand=True, fill=tk.BOTH, side=tk.RIGHT, anchor=tk.N,padx=10, pady=10)

#ListBox para mostrar las palabras ingresadas
gameListFrame = tk.Frame(rightGameFrame, bg="white")
gameListFrame.pack(fill=tk.BOTH, expand=True)
gameListScroll = tk.Scrollbar(gameListFrame, orient=tk.VERTICAL)
gameListbox = tk.Listbox(gameListFrame, width=1, yscrollcommand=gameListScroll.set, bg="#DAF7DC", fg="black", font=("Arial", 16, "bold"))
gameListScroll.config(command=gameListbox.yview)
gameListScroll.pack(side=tk.RIGHT, fill=tk.Y) 
gameListbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) 

#Boton para encontrar las palabras con prolos 
solve_btn = tk.Button(rightGameFrame, text="Solucionar", command=solucion,  bg="#9EE493", fg="#2F4858")
solve_btn.pack(expand=False, fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, padx=10, pady=10)


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


cargarGameFrame()

#pintar_matriz(emptyMatrix, leftGameFrame)
# pintar_matriz(data, leftGameFrame)
# cambiarColor(leftGameFrame, 0, 0, "red")

window.mainloop()