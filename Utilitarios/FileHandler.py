'''
Instituto Tecnologico de Costa Rica
Escuela de Ingenieria en Computacion
Curso: Lenguages de Programacion

Programa: Manejador de Archivos
Lenguaje: Python
Profesor: Oscar Viquez Acuña 

Estudiante: Josue Chaves Araya - 2015094068

I Semestre 2023
'''

import json
from tkinter import filedialog as fd

#Este código escribe en un archivo .pl los conocimientos de la sopa de letras

#funcion para escribir una lista de strings en un archivo
def storeKnowledge(list, fileName):
    file = open(fileName, 'w')
    for e in list:
        file.write(e)
    file.close()

#Funcion que abre un archivo json que contiene la matriz y la retorna
def getInputDataFromJson(file_path, inputData):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data[inputData]
        except:
            print(f"No se encontro \"{inputData}\" el json")
            return None


# Ejemplo de uso
# matrixPath = './../DatosEntrada/matriz.json'
# palabrasPath = './../DatosEntrada/palabras.json'

# matrix = getInputDataFromJson(palabrasPath,"palabras")
# print(matrix)

