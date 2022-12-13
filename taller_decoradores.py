"""Implementar la función get_avg que calcule el promedio de una lista de números:"""

# lista= [i for i in range(1,21)]

# def get_avg():
#     for i in lista:
#         suma= sum(lista)
#         resultado= suma/len(lista)
#         return resultado

# print(get_avg())

"""Implementar la función get_avg que calcule el promedio de una lista de números:

def get_avg(lista):
  lista = [10, 40, 20, 45, 25, 35, 15]
  pass
La función get_avg retorna un float.

Asimismo implementar un decorador que permita imprimir los siguientes mensajes:

Inicio del cálculo del promedio de la lista de números.
El cálculo ha finalizado.
Entre ambos mensajes debe realizarse el cálculo del promedio de números."""

# def decorador(funcion):
#     def interior():
#         print("nicio del cálculo del promedio de la lista de números.")
#         funcion()
#         print("El cálculo ha finalizado.")
#     return interior

# @decorador
# def get_avg():
#     lista= [i for i in range(1,21)]
#     suma= sum(lista)
#     resultado= suma/len(lista)
#     print(f'El promedio es: {resultado} ')

# get_avg()

"""Escriba un programa que dada una entrada numérica por el usuario, ingrese a una función que duplique el valor y sea 
retornado en forma de string o cadena. Utilice tipos tanto para las variables como para las funciones.
1ro= input de numero ingresado por el usuario
2do= crear funcion que duplique el valor del numero ingresado
3ro= retornar le valor duplicado en tipo de dato String.

"""
# def decorador(func):
#     def interior():
#         print(f"El valor doble del numero en String es: {type(func())}")
#     return interior

# @decorador
# def numero_duplicado():
#     numero= float(input("Ingrese un numero: "))
#     resultado= numero * 2
#     print(str(resultado))
# numero_duplicado()

# ###########3SOLUCION FINAL
# def conversion(i: float) -> str:
#     return str(i*2)

# x: float = float(input("Ingrese un numero: "))
# print(f'El doble del numero es: {conversion(x)}')
# print(f'Y es de tipo: {type(conversion(x))}')

"""Cree una función con anotaciones, que tome una palabra y duplique sus letras y las retorne en una lista.

Ejemplo:

Ingrese una palabra: hola

Retorna: ['h','h','o','o','l','l','a','a']
https://campusvirtual.ull.es/ocw/pluginfile.php/8877/mod_imscp/content/3/caractersticas_de_una_funcin.html
1ro= input()
convertir la palabra en una lista
recorrer i en la lista
duplicar cada i en la lista
retornar la lista."""

# lista_final= []
# palabra= list(input("Ingrese una palabra: "))
# for i in palabra:
#     def letras_duplicadas(i: int) -> list:
#         resultado= i * 2
#         lista_final.append(resultado)
#         return lista_final

#     print(letras_duplicadas(i))

##### SOLUCION FINAL
# from typing import List
# def convertir_a_lista(p: str) -> List[str]:
#     l: list= []

#     for i in p:
#         l.append(i)   ##aqui se esta duplicando las letras en vez de i*2
#         l.append(i)    #aqui se esta duplicando las letras en vez de i*2
#     return l

# palabra: str = input("Ingrese una palabra: ")
# print(convertir_a_lista(palabra))

"""Dada la función "calc_par_impar" que retorna un booleano, dependiendo si el número ingresado es par o impar, cree un decorador
que imprima que tipo de número a recibido la función.

def calc_par_impar(n):
    if n % 2 == 0:
        return True
    return False"""
# n= float(input("ingrese un numero: "))
# def decorador(func):
#     def intermedio():
#         if func(n) == True:
#             print("El numero es par")
#         else:
#             print("El numero es impar")
#     return intermedio(n)

# @decorador
# def calc_par_impar(n):
#     if n % 2 == 0:
#         return True
#     return False

# print(calc_par_impar(n))

# def deco1(func1):
#     def intermedio(*args):
#         if func1(*args):
#             print("El numero es par")
#         else:
#             print("El numero es impar")
#     return intermedio

# @deco1
# def calc_par_impar(n):
#     if n % 2 == 0:
#         return True
#     return False
# numero = float(input("ingrese un numero: "))
# calc_par_impar(numero)

"""Cree una función decoradora deco1 que muestre el siguiente flujo, para cualquier número ingresado, por ejemplo para el número 30:

Hola, estoy decorando esta función.

Ingresaste el numero 30

Terminar de decorar

def deco1(funcParametro):
  pass

@deco1
def mostrar(n):
    print("Ingresaste el número", n)

mostrar(30)"""

def deco1(funcParametro):
    def interno(*args):
        print("Hola estoy decorando esta funcion")
        funcParametro(*args)
        print("Terminé de decorar.")
    return interno

@deco1
def mostrar(n):
    print("Ingresaste el número", n)

mostrar(30)
