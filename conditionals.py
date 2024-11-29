"""
Condicionales

Van a realizar una acción en función de una evaluación

if
if-else
if-elif-else

"""
"""
nombre = "Guillermo"
edad = 10 

# if [evaluacion que dará True o False] :
# operadores logicos [OR AND NOT]
if edad >= 18 and nombre != "Guillermo":
    print("Bienvenido")
elif edad >= 10:
    print("Ve a la sala de juegos")
else:
    print("Adiós")
   """ 
    
""" Genera un codigo en python que le pregunte al usuario por su país y le responda con un saludo típico, usando solo condicionales.

Si es Colombia: Hola Parce
Si es Chile: Hola poh
Si es Venezuela: Hola chamo

"""

pais = input("Ingresa tu país(Colombia, Chile, Venezuela o Argentina: " ).lower()
if pais == "colombia":
    print("Hola Parce")
elif pais == "chile":
    print("Buena poh")
elif pais == "venezuela":
    print("Hola Chamo")
elif pais == "argentina":
    print("Hola Che")
else:
    print("No eres parte de CloudMasters")
