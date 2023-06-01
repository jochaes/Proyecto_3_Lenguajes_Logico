'''
Instituto Tecnologico de Costa Rica
Escuela de Ingenieria en Computacion
Curso: Lenguages de Programacion

Programa: Gnenrador de Matrices y Conocimiento
Lenguaje: Python
Profesor: Oscar Viquez Acuña 

Estudiante: Josue Chaves Araya - 2015094068

I Semestre 2023
'''

import random

# Función para generar una sopa de letras
def generar_sopa_letras(tamano, palabras):
    # Crear una matriz vacía de tamaño NxN
    sopa_letras = [[' ' for _ in range(tamano)] for _ in range(tamano)]
    
    # Colocar las palabras en la matriz (horizontal, vertical y diagonal)
    for palabra in palabras:
        palabra = palabra.upper()
        colocada = False
        while not colocada:
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - 1)
            direccion = random.choice(['horizontal', 'vertical', 'diagonal'])
            
            # Verificar si la palabra puede ser colocada en esa posición y dirección
            if validar_posicion(sopa_letras, palabra, fila, columna, direccion):
                colocar_palabra(sopa_letras, palabra, fila, columna, direccion)
                colocada = True
    
    # Rellenar los espacios vacíos con letras aleatorias
    llenar_espacios_vacios(sopa_letras)
    
    return sopa_letras

def validar_posicion(sopa_letras, palabra, fila, columna, direccion):
    tamano = len(sopa_letras)
    longitud = len(palabra)
    
    # Verificar si la palabra cabe en la posición y dirección
    if direccion == 'horizontal' and columna + longitud > tamano:
        return False
    elif direccion == 'vertical' and fila + longitud > tamano:
        return False
    elif direccion == 'diagonal' and (fila + longitud > tamano or columna + longitud > tamano):
        return False
    
    # Verificar si no hay letras conflictivas en la posición y dirección
    for i in range(longitud):
        if direccion == 'horizontal':
            if sopa_letras[fila][columna + i] != ' ' and sopa_letras[fila][columna + i] != palabra[i]:
                return False
        elif direccion == 'vertical':
            if sopa_letras[fila + i][columna] != ' ' and sopa_letras[fila + i][columna] != palabra[i]:
                return False
        elif direccion == 'diagonal':
            if sopa_letras[fila + i][columna + i] != ' ' and sopa_letras[fila + i][columna + i] != palabra[i]:
                return False
    
    return True

def colocar_palabra(sopa_letras, palabra, fila, columna, direccion):
    for i, letra in enumerate(palabra):
        if direccion == 'horizontal':
            sopa_letras[fila][columna + i] = letra
        elif direccion == 'vertical':
            sopa_letras[fila + i][columna] = letra
        elif direccion == 'diagonal':
            sopa_letras[fila + i][columna + i] = letra

def llenar_espacios_vacios(sopa_letras):
    tamano = len(sopa_letras)
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in range(tamano):
        for j in range(tamano):
            if sopa_letras[i][j] == ' ':
                sopa_letras[i][j] = random.choice(letras)


# Función para generar el conocimiento de la sopa de letras en Prolog
def generarHechosProlog(matrix, n):
    facts = []
    for row in range(n):
        for col in range(n):
            fact = f"location({(matrix[row][col]).lower()},{row},{col}).\n"
            facts.append(fact)
    return facts


# Ejemplo de uso
tamano = 12
palabras = ['HOLA', 'MUNDO', 'PALA', 'PROLOG', 'TIENDA', 'JUEGO', 'PALABRA', 'CASA', 'PERRO','COCINA']
sopa = generar_sopa_letras(tamano, palabras)

print(sopa)


# # Imprimir la sopa de letras generada
# for fila in sopa:
#     print(' '.join(fila))

# facts = prologFactsGenerator(sopa, tamano)
# for fact in facts:
#     print(fact)
