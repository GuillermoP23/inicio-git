"""
ciclo while es una sentencia que repetirá un conjunto de instrucciones mientras que una condición sea verdadera.


"""

contador = 1

while contador < 10 :
    print(contador)
    contador+=1 #incrementando o sumando 1 en cada iteración
    


"""
Pide al usuario que ingrese todos los estudiantes de un curso 
y al final debes imprimir un saludo para cada uno

ejemplo de entreda:
Laura
Felipe
Oscar

ejemplo de salida:
Hola Laura
Hola Felipe
Hola Oscar
"""

# crear lista vacia
estudiantes = []
#preguntarle si quiere agregar estudiantes
opcion = input("Necesita agregar estudiantes?(Si o No): ")

while opcion != "No":
#de forma provisional guardamos el estudiante en una variable
    nombre = input("Ingresa un estudiante: ")
    
    estudiantes.append(nombre)
#voy a preguntarle al usuario si quiere acabar
    opcion = input("Quiere continuar?(Si o No): ")
    if opcion == "No":
        break # detiene el ciclo
print(estudiantes)

for estudiante in estudiantes:
    print(f"Bienvenid@, {estudiante}")
    