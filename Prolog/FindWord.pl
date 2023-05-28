/*
Instituto Tecnologico de Costa Rica
Escuela de Ingenieria en Computacion
Curso: Lenguages de Programacion

Programa: Buscador de palabras en una matriz de letras
Lenguaje: Prolog
Profesor: Oscar Viquez Acuña 

Estudiante: Josue Chaves Araya - 2015094068

I Semestre 2023
*/

:-consult('Matrix.pl').

% Predicado para buscar todas las apariciones de la palabra en la matriz
findWord(Word,Solutions) :-
  findall(Path, findWord_Aux(Word, Path), Solutions),!. 

% Predicado para buscar una palabra en la matriz
findWord_Aux(Word,[Start|Path]) :-
    atom_chars(Word, [L1|Left]),             % Divide la palabra en una lista de caracteres
    location(L1,R,C),                        % Obtiene la posicion de la primera letra de la palabra
    Start = (R,C),                           % Crea una tupla con la posicion del punto de partida
    findWord_Matrix(Left, [R,C], Path).


findWord_Matrix([], _, []).  
findWord_Matrix([Letter|Left], LastPosition, [Position|LeftPositions]) :-
    location(Letter, Row, Column),                                         %Obtiene la posicion de la letra en la matriz
    adjacent(LastPosition, [Row, Column]),                               % Verifica si la posicion actual es adyacente a la posicion anterior
    Position = (Row, Column),                                             % Crea una tupla con la posicion
    findWord_Matrix(Left, [Row, Column], LeftPositions).

% Predicado para verificar si dos posiciones son adyacentes
adjacent([R1, C1], [R2, C2]) :-
    abs(R1 - R2) =< 1,                % Verifica que la diferencia de filas sea menor o igual a 1
    abs(C1 - C2) =< 1,                % Verifica que la diferencia de columnas sea menor o igual a 1
    (R1 =\= R2 ; C1 =\= C2).          % Verifica que no sean la misma posicion

