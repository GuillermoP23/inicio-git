"""
print("Bienvenido, las opciones son: ")
print("1. Crear un libro")
print("2. Actualizar un libro")
print("3. Eliminar un libro")
print("4. Consultar un libro")
print("5. Mostrar todo el inventario")
print("6. Salir") """


opcion = 0

while opcion!=6:
    print("Bienvenido, las opciones son: ")
    print("1. Crear un libro")
    print("2. Actualizar un libro")
    print("3. Eliminar un libro")
    print("4. Consultar un libro")
    print("5. Mostrar todo el inventario")
    print("6. Salir") #solo saldrá del ciclo si es 6

    opcion = int(input("Ingresa una opción que quieras hacer: "))


    if opcion == 1:
        print("Vamo' a crear")
    elif opcion == 2:
        print("Vamo' actualizar")
    elif opcion == 3:
        print("Vamo' eliminar")
    elif opcion == 4:
        print("Vamo' consultar")
    elif opcion == 5:
        print("Vamo' mostrar")
    elif opcion == 6:
        print("Hasta luego")
    else:
        print("Ingresa una opción válida")
    