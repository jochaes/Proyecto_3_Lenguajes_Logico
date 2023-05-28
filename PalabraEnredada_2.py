from Utilitarios.PrologLink import *
from Utilitarios.MatrixGenerator import *
from Utilitarios.FileHandler import *
import tkinter as tk

# ################################## User Interface ##################################

# window = tk.Tk()
# window.title("Palabra Enredada")
# window.geometry("640x360")
# # window.maxsize(1024, 768)
# # window.minsize(900, 675)
# window.config(bg="skyblue")



# ################################## Functions ##################################



# def loadGameFrame():
#     nombre = entry.get()
#     label_nombre.config(text="Nombre: " + nombre)
#     startFrame.pack_forget()  # Ocultar frame_a
    
#     gameFrame.pack()  # Mostrar frame_b

# def loadStartFrame():
#     gameFrame.pack_forget()  # Ocultar frame_b
#     startFrame.pack()  # Mostrar frame_a


# ################################## Start Frame ##################################
# lbIndex = 0
# wordEvent = False

# def addWordListBox(self, event=None):

#     inputWord = entry.get()
#     entry.delete(0, tk.END)
#     listbox.insert(tk.END, inputWord)
#     print(inputWord)
    
# def onselect(evt):
#     # Note here that Tkinter passes an event object to onselect()
#     w = evt.widget
#     lbIndex = w.curselection()[0]
#     value = w.get(lbIndex)
#     print('You selected item %d: "%s"' % (lbIndex, value))
    
    

# #Ventana de Incio 
# startFrame = tk.Frame(window, bg="white")
# startFrame.grid(row=0, column=0, padx=1, pady=1)

# # Label para el Titulo del Juego
# gameTitle_label = tk.Label(startFrame, text="Bienvenido a Palabra Enredada", font=("Arial", 20), bg="white")
# gameTitle_label.grid(row=0, column=0, padx=10, pady=5)

# inputWord_label = tk.Label(startFrame, text="Ingrese las palabras:", bg="white")   
# inputWord_label.grid(row=1, column=0, padx=10, pady=5)

# # Input para ingresar las palabras
# entry = tk.Entry(startFrame)
# entry.grid(row=2, column=0, padx=10, pady=5)
# #Cuando se presiona enter
# entry.bind("<Return>", addWordListBox)

# #ListBox para mostrar las palabras ingresadas
# listScroll = tk.Scrollbar(startFrame, orient=tk.VERTICAL)
# listbox = tk.Listbox(startFrame, width=50, height=10, yscrollcommand=listScroll.set)
# listScroll.config(command=listbox.yview)
# listScroll.grid(row=3, column=1, sticky=tk.N+tk.S)
# listbox.grid(row=3, column=0, padx=10, pady=5)
# listbox.bind('<<ListboxSelect>>', onselect)

# # Boton para cargar la ventana del juego
# button_a = tk.Button(startFrame, text="Iniciar Palabras Enredadas", command=loadGameFrame)
# button_a.grid(row=4, column=0, padx=10, pady=5)





# ################################## Game Frame ##################################

# gameFrame = tk.Frame(window, bg="darkblue")
# # gameFrame.grid(row=0, column=0, padx=10, pady=5)
# startFrame.pack()

# label_nombre = tk.Label(gameFrame, text="")
# label_nombre.pack()

# button_b = tk.Button(gameFrame, text="Mostrar Ventana A", command=loadStartFrame)
# button_b.pack()


#Generación de la Matriz de Letras
tamano = 6 
palabras = ['hola', 'mundo', 'adios']
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




# window.mainloop()