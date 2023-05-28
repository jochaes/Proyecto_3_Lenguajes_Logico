from Utilitarios.PrologLink import *
from Utilitarios.MatrixGenerator import *
from Utilitarios.FileHandler import *
import tkinter as tk
from tkinter import messagebox

################################## Global Vars ##################################
lbIndex = 0         #Listbox Index
eventT = False      #Event trigger to change a word in the listbox
MATRIX_SIZE = 10    #Matrix Size

################################## User Interface ##################################

window = tk.Tk()
window.title("Palabra Enredada")
window.geometry("640x360")
window.resizable(False, False)
# window.maxsize(1024, 768)
# window.minsize(900, 675)
window.config(bg="skyblue")



################################## Functions ##################################



def loadGameFrame():
    nombre = entry.get()
    label_nombre.config(text="Nombre: " + nombre)
    startFrame.pack_forget()  # Ocultar frame_a
    
    gameFrame.pack()  # Mostrar frame_b

def loadStartFrame():
    gameFrame.pack_forget()  # Ocultar frame_b
    startFrame.pack()  # Mostrar frame_a

# def showMessage(title, message):
#     #Colocar messagebox en el centro de la ventana
#     msgbx = tk.messagebox.showinfo(title, message, parent=window)
    
def showMessage(title, message):
        self = window
        top = tk.Toplevel(self)
        top.details_expanded = False
        top.title(title)
        #Store the size of the window in a string
        print(window.winfo_width())
        
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



def addWordListBox(self, event=None):
    global lbIndex
    global eventT
    inputWord = entry.get()

    if len(inputWord) > MATRIX_SIZE:
        msg = f"La palabra no puede ser mayor a {MATRIX_SIZE} letras"
        showMessage("Error", msg)
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
        listbox.insert(tk.END, inputWord)
        print(inputWord)

'''
Cuando el Usuario selecciona una palabra de la lista, se activa el evento onselect
para cargar la palabra en el Entry y poder cambiarla o eliminarla(Si borra toda la palabra).
'''
def onselect(evt):
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
    
    

#Ventana de Incio 
startFrame = tk.Frame(window, bg="white")
startFrame.grid(row=0, column=0, padx=1, pady=1)

# Label para el Titulo del Juego
gameTitle_label = tk.Label(startFrame, text="Bienvenido a Palabra Enredada", font=("Arial", 20),bg="white", fg="black")
gameTitle_label.grid(row=0, column=0, padx=10, pady=5)

inputWord_label = tk.Label(startFrame, text="Ingrese las palabras:", bg="white", fg="black")   
inputWord_label.grid(row=1, column=0, padx=10, pady=5)

# Input para ingresar las palabras
entry = tk.Entry(startFrame,bg="white", fg="black")
entry.grid(row=2, column=0, padx=10, pady=5)
#Cuando se presiona enter
entry.bind("<Return>", addWordListBox)

#ListBox para mostrar las palabras ingresadas
listScroll = tk.Scrollbar(startFrame, orient=tk.VERTICAL)
listbox = tk.Listbox(startFrame, width=50, height=10, yscrollcommand=listScroll.set, bg="white", fg="black")
listScroll.config(command=listbox.yview)
listScroll.grid(row=3, column=1, sticky=tk.N+tk.S)
listbox.grid(row=3, column=0, padx=10, pady=5)
listbox.bind('<<ListboxSelect>>', onselect)

#Hacer una lista con 10 palabras aleatorias e insertarlas en el listbox
palabras = ['hola', 'mundo', 'adios', 'ropa', 'casa','camion', 'perro', 'gato', 'pajaro', 'pescado']
for palabra in palabras:
    listbox.insert(tk.END, palabra)


# Boton para cargar la ventana del juego
button_a = tk.Button(startFrame, text="Iniciar Palabras Enredadas", command=loadGameFrame, bg="white", fg="black")
button_a.grid(row=4, column=0, padx=10, pady=5)





################################## Game Frame ##################################

gameFrame = tk.Frame(window, bg="darkblue")
# gameFrame.grid(row=0, column=0, padx=10, pady=5)
startFrame.pack()

label_nombre = tk.Label(gameFrame, text="")
label_nombre.pack()

button_b = tk.Button(gameFrame, text="Mostrar Ventana A", command=loadStartFrame)
button_b.pack()


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

window.mainloop()