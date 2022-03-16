"""
1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""
def num_max(n1:int ,n2:int):
    if n1 > n2:
        return n1
    else:
        return n2
print(num_max(5,2))

"""
2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(n1:int,n2:int,n3:int):
    num = num_max(n1,n2)
    num_final = num_max(n3,num)

    return num_final
print(max_de_tres(5,8,2))

"""
3 - Definir una función que calcule la longitud de una lista o una cadena dada.
(Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud_lista_cadena(cadena:str):
    cnt = 0
    for n in cadena:
        cnt += 1

    return cnt
print(longitud_lista_cadena([1,2,3,4,5,6,7,1,2312,4]))
print(longitud_lista_cadena("Hola mundo!"))

"""
4 - Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""

def vocal(char):
    lista_char = ['a','e','i','o','u']
    if char in lista_char:
        return True
    else:
        return False
print(vocal('a'))
print(vocal('3'))

"""
5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum(lista:list):
    suma_final = 0
    for n in lista:
        suma_final += n
    return suma_final

def multip(lista:list):
    multip_final = 1
    for n in lista:
        multip_final *= n
    return multip_final

print(sum([1,2,3,4]))
print(multip([1,2,3,4]))

"""
6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""

def inversa(cadena:str):
    return cadena[::-1]

print(inversa('estoy probando'))

"""
7 - Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(cadena:str):
    if cadena == inversa(cadena):
        return True

print(es_palindromo('radar'))

"""
8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.
"""

def superposicion(lista1:list,lista2:list):
    cnt = 0
    for n in lista1:
        for c in lista2:
            if c == n:
                cnt += 1
    if cnt > 0:
        return True
    else:
        return False

print(superposicion([1,2,3],[4,1,6]))
print(superposicion([1,2,3],[4,5,6]))

"""
9 - Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n1:int,c1:str):
    return c1 * n1

print(generar_n_caracteres(5,'x'))

"""
10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""

def procedimiento(lista:list):
    for n in lista:
        histograma = '*' * n
        print(f'{histograma}')
print(procedimiento([4,9,7]))