import tkinter as tk

def mostrar_ventana_a():
    ventana = tk.Tk()

    def cargar_ventana_b():
        nombre = entry.get()
        label_nombre.config(text="Nombre: " + nombre)
        frame_a.pack_forget()  # Ocultar frame_a
        frame_b.pack()  # Mostrar frame_b

    def mostrar_ventana_a():
        frame_b.pack_forget()  # Ocultar frame_b
        frame_a.pack()  # Mostrar frame_a

    ventana.title("Ventana Principal")

    # Frame A
    frame_a = tk.Frame(ventana)
    frame_a.pack()

    label_a = tk.Label(frame_a, text="Ingrese un nombre:")
    label_a.pack()

    entry = tk.Entry(frame_a)
    entry.pack()

    button_a = tk.Button(frame_a, text="Cargar Ventana B", command=cargar_ventana_b)
    button_a.pack()

    # Frame B
    frame_b = tk.Frame(ventana)
    frame_b.pack()

    label_nombre = tk.Label(frame_b, text="")
    label_nombre.pack()

    button_b = tk.Button(frame_b, text="Mostrar Ventana A", command=mostrar_ventana_a)
    button_b.pack()

    mostrar_ventana_a()

    ventana.mainloop()

# Inicio del programa
mostrar_ventana_a()
