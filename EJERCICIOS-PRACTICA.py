"""
Ejercicio 1: Suma de números del 1 al 10
Usa un ciclo for para calcular la suma de los números del 1 al 10

"""
#range(inicio,final)
#range(inicio, final,salto)
suma=0
for numero in range(1,11):
    suma += numero
    print(suma)
    
"""
Ejercicio 2: Tablas de multiplicar
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).

"""

multiplicación=0
for numero in range(1,11):
    multiplicacion = (numero*5)
    print(f"{numero}x5={multiplicacion}")
    
"""
Ejercicio 3: Contar vocales en una palabra
Pide al usuario una palabra y cuenta cuántas vocales tiene.

"""
palabra = input("Ingresa una palabra: ")
contador = 0
for vocales in palabra:
    if vocales == "a" or vocales == "e" or vocales=="i" or vocales=="o" or vocales=="u":
       contador = contador+1
print(f"la cantidad de vocales es {contador}")
    
"""
Ejercicio 4: Encontrar el número mayor
Dado un listado de números, encuentra el mayor usando un ciclo y un condicional.

"""
listadoNumeros = [3,4,8,9,10]
valorAnterior = 0
 
for valor in listadoNumeros:
    if valor > valorAnterior:
        valorAnterior = valor

print(f"El mayor es {valor}")

"""Ejercicio 5: Contar hasta que el usuario lo detenga
Usa un ciclo while para imprimir números empezando desde 1, hasta que el usuario escriba stop.
"""
contador = 1
opcion_usuario = ""
while opcion_usuario =! "stop":
    print(contador)



    
    


"""Ejercicio 6: Adivina el número
Crea un programa donde el usuario adivine un número entre 1 y 10.
"""
valor_correcto = 5
valor_elegido = int(input("Adivina el numero correcto(1 al 10): "))

if valor_elegido == valor_correcto:
    print("Acertaste")
else:
    print("Perdiste")


"""Ejercicio 7: Número par o impar
Pide al usuario un número y determina si es par o impar.
"""
numero_usuario = int(input("Ingresa un número: "))

if numero_usuario%2 == 0:
    print("El número seleccionado es par")
else:
    print("El número seleccionado es impar")
    
    
"""
Ejercicio 8: Números hasta N
Pide al usuario un número N y usa un ciclo for para imprimir todos los números desde 1 hasta N.
"""
numero = int(input("Ingresa un número"))

for x in range(1, numero+1):
    print(x)




    