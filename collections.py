"""
listas son una colección ordenada de elementos

son mutables(es decir puedo cambiar un elemento en particular de la lista o agregar un elemeto nuevo)

"""

myFruitList = ["Pera", "Banana", "Mango"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

#cambio la mango por un melón

myFruitList[2] = "Melón"

print(myFruitList)

#metodos de las listas .append() permite agregar un elemento a la lista

#añadir tomate con .remove() remueve el primer elemento que coincide con ese valor.

myFruitList.append("Tomate")
print(myFruitList)

#remover banana

myFruitList.remove("Banana")
print(myFruitList)

"""
Tupla

Es una colección ordenada de elementos
Es inmutable(es una lista que no puede cambiar)

"""

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#acceder a un elemento por posición

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])


"""
diccionarios 
es una coleccion de elementos de clave valor mutables

clave: entero  string, es unico y si se repite se sobrescribe sobre la primera, es decir se toma el ultimo.
valor: cualquier tipo de dato, este se puede repetir.
"""

fondosRestart = {
    "Akua" : "rojo",
  "Saanvi" : "negro",
  "Paulo" : "verde"
}
print(fondosRestart)
print(type(fondosRestart))

#traer el fondo de Paulo pero debe hacerce por medio de las claves
print(fondosRestart["Paulo"])

#agregar un elemento solo creando la clave, se agrega al final

fondosRestart["Gustavo"] = "gris"

print(fondosRestart)

