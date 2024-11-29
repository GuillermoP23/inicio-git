#Números Proporcionados: 2, 3, 7, 5, 11 
#Valor Objetivo: 50

#jerarquia PAPOMUDAS
#PARENTESIS
#POTENCIA
#MULTIPLICACION & DIVISION
#SUMA & RESTA

print("Python tiene 3 tipos de datos númericos: int, float, complex")

valor = 5

print(valor)

print(type(valor))

print(f"Hola, el valor es {valor} y su tipo de dato es {type(valor)}")   # con f se puede concatenar string con variables

#float = numeros decimales

valor = 4.555

print(f"Hola, el valor es {valor} y su tipo de dato es {type(valor)}")

#complex = 4j 25j 4.5j

valor = 4j

print(f"Hola, el valor es {valor} y su tipo de dato es {type(valor)}")

#bool = True & False

valor = True

print(f"Hola, el valor es {valor} y su tipo de dato es {type(valor)}")

"""
CAST
Conversion tipos de datos
"""

a = 45
b = float(a)

print(f"A es de tipo {type(a)} ; B es de tipo {type(b)}")
