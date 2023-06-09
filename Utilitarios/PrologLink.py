'''
Instituto Tecnologico de Costa Rica
Escuela de Ingenieria en Computacion
Curso: Lenguages de Programacion

Programa: Conexión con Prolog
Lenguaje: Python
Profesor: Oscar Viquez Acuña 

Estudiante: Josue Chaves Araya - 2015094068

I Semestre 2023
'''

# Tuve varios errores con la libreria pyswip 
# Acá nos dicen cómo arreglaro: https://swi-prolog.discourse.group/t/how-to-brew-install-swi-prolog-8-4-3-when-9-0-0-is-out/5973/4
#instalar pyswip con el siguiente comando: python3 -m pip install git+https://github.com/yuce/pyswip@master#egg=pyswip

from pyswip import Prolog

def obtenerCoordenadas(coordStr):
    coordStr = coordStr[1:]         #Quita la ',' de cada uno de los elementos de la lista
    coordTuple = eval(coordStr)     #Convierte el string a una tupla
    return coordTuple

def consultarPalabra(word):
    prolog = Prolog()                                               #Crea el objeto prolog
    prolog.consult("./Prolog/FindWord.pl")                         #Carga el archivo BuscarPalabra.pl

    results = list(prolog.query('findWord("'+word+'", Solutions).'))    #Consulta a prolog 
    
    path = []
    
    for result in (results[0])['Solutions']:
        result = map(obtenerCoordenadas, result) #Convierte cada uno de los elementos de la lista en una tupla
        path.append(list(dict.fromkeys(result))) #Convierte el resultado en una lista y elimina los elementos repetidos        
    return path


# resultado = wordPath('hola') 
# print(resultado[0])


