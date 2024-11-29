"""
ciclo for

se usa cuando sé exactamente cuando va a parar el ciclo.

es ideal para recorrer listas, tuplas y diccionarios, etc. secuencias.

"""

lista= ["Dinosaurios", 23, True, 45.5,  "Amazon"]

# for [variable de iteracion] in [lista]

for elemento in lista:
    print(f"El elemento es {elemento} y su tipo de dato es {type(elemento)}")
    
    
    
#imprimir solo números pares    %2 se utiliza para obtener el resto de una division entre dos números
numeros = [2,45,19,13,178]

for x in numeros:
    if x %2 == 0:
        print(f"los numeros pares son: {x} ")
    