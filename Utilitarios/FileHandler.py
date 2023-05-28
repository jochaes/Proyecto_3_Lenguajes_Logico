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


#Este código escribe en un archivo .pl los conocimientos de la sopa de letras

#funcion para escribir una lista de strings en un archivo
def storeKnowledge(list, fileName):
    file = open(fileName, 'w')
    for e in list:
        file.write(e)
    file.close()
