{"changed":true,"filter":false,"title":"EJERCICIOS-PRACTICA.py","tooltip":"/EJERCICIOS-PRACTICA.py","value":"\"\"\"\nEjercicio 1: Suma de números del 1 al 10\nUsa un ciclo for para calcular la suma de los números del 1 al 10\n\n\"\"\"\n#range(inicio,final)\n#range(inicio, final,salto)\nsuma=0\nfor numero in range(1,11):\n    suma += numero\n    print(suma)\n    \n\"\"\"\nEjercicio 2: Tablas de multiplicar\nEscribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).\n\n\"\"\"\n\nmultiplicación=0\nfor numero in range(1,11):\n    multiplicacion = (numero*5)\n    print(f\"{numero}x5={multiplicacion}\")\n    \n\"\"\"\nEjercicio 3: Contar vocales en una palabra\nPide al usuario una palabra y cuenta cuántas vocales tiene.\n\n\"\"\"\npalabra = input(\"Ingresa una palabra: \")\ncontador = 0\nfor vocales in palabra:\n    if vocales == \"a\" or vocales == \"e\" or vocales==\"i\" or vocales==\"o\" or vocales==\"u\":\n       contador = contador+1\nprint(f\"la cantidad de vocales es {contador}\")\n    \n\"\"\"\nEjercicio 4: Encontrar el número mayor\nDado un listado de números, encuentra el mayor usando un ciclo y un condicional.\n\n\"\"\"\nlistadoNumeros = [3,4,8,9,10]\nvalorAnterior = 0\n \nfor valor in listadoNumeros:\n    if valor > valorAnterior:\n        valorAnterior = valor\n\nprint(f\"El mayor es {valor}\")\n\n\"\"\"Ejercicio 5: Contar hasta que el usuario lo detenga\nUsa un ciclo while para imprimir números empezando desde 1, hasta que el usuario escriba stop.\n\"\"\"\ncontador = 1\nopcion_usuario = \"\"\nwhile opcion_usuario =! \"stop\":\n    print(contador)\n\n\n\n    \n    \n\n\n\"\"\"Ejercicio 6: Adivina el número\nCrea un programa donde el usuario adivine un número entre 1 y 10.\n\"\"\"\nvalor_correcto = 5\nvalor_elegido = int(input(\"Adivina el numero correcto(1 al 10): \"))\n\nif valor_elegido == valor_correcto:\n    print(\"Acertaste\")\nelse:\n    print(\"Perdiste\")\n\n\n\"\"\"Ejercicio 7: Número par o impar\nPide al usuario un número y determina si es par o impar.\n\"\"\"\nnumero_usuario = int(input(\"Ingresa un número: \"))\n\nif numero_usuario%2 == 0:\n    print(\"El número seleccionado es par\")\nelse:\n    print(\"El número seleccionado es impar\")\n    \n    \n\"\"\"\nEjercicio 8: Números hasta N\nPide al usuario un número N y usa un ciclo for para imprimir todos los números desde 1 hasta N.\n\"\"\"\nnumero = int(input(\"Ingresa un número\"))\n\nfor x in range(1, numero+1):\n    print(x)\n\n\n\n\n    ","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":51,"column":5},"end":{"row":51,"column":6},"action":"remove","lines":[" "],"id":891},{"start":{"row":51,"column":4},"end":{"row":51,"column":5},"action":"remove","lines":["e"]},{"start":{"row":51,"column":3},"end":{"row":51,"column":4},"action":"remove","lines":["l"]},{"start":{"row":51,"column":2},"end":{"row":51,"column":3},"action":"remove","lines":["i"]},{"start":{"row":51,"column":1},"end":{"row":51,"column":2},"action":"remove","lines":["h"]},{"start":{"row":51,"column":0},"end":{"row":51,"column":1},"action":"remove","lines":["w"]}],[{"start":{"row":84,"column":40},"end":{"row":85,"column":0},"action":"insert","lines":["",""],"id":892},{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"insert","lines":["i"],"id":893},{"start":{"row":86,"column":1},"end":{"row":86,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":86,"column":2},"end":{"row":86,"column":3},"action":"insert","lines":[" "],"id":894},{"start":{"row":86,"column":3},"end":{"row":86,"column":4},"action":"insert","lines":["n"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"insert","lines":["u"]},{"start":{"row":86,"column":5},"end":{"row":86,"column":6},"action":"insert","lines":["m"]},{"start":{"row":86,"column":6},"end":{"row":86,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":86,"column":7},"end":{"row":86,"column":8},"action":"insert","lines":["r"],"id":895},{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"insert","lines":["o"]}],[{"start":{"row":86,"column":9},"end":{"row":86,"column":10},"action":"insert","lines":[" "],"id":896}],[{"start":{"row":86,"column":10},"end":{"row":86,"column":11},"action":"insert","lines":["<"],"id":897}],[{"start":{"row":86,"column":10},"end":{"row":86,"column":11},"action":"remove","lines":["<"],"id":898},{"start":{"row":86,"column":9},"end":{"row":86,"column":10},"action":"remove","lines":[" "]},{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"remove","lines":["o"]},{"start":{"row":86,"column":7},"end":{"row":86,"column":8},"action":"remove","lines":["r"]},{"start":{"row":86,"column":6},"end":{"row":86,"column":7},"action":"remove","lines":["e"]},{"start":{"row":86,"column":5},"end":{"row":86,"column":6},"action":"remove","lines":["m"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["u"]},{"start":{"row":86,"column":3},"end":{"row":86,"column":4},"action":"remove","lines":["n"]},{"start":{"row":86,"column":2},"end":{"row":86,"column":3},"action":"remove","lines":[" "]},{"start":{"row":86,"column":1},"end":{"row":86,"column":2},"action":"remove","lines":["f"]},{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"remove","lines":["i"]},{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":85,"column":0},"end":{"row":86,"column":0},"action":"insert","lines":["",""],"id":899},{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"insert","lines":["f"]},{"start":{"row":86,"column":1},"end":{"row":86,"column":2},"action":"insert","lines":["o"]},{"start":{"row":86,"column":2},"end":{"row":86,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":86,"column":3},"end":{"row":86,"column":4},"action":"insert","lines":[" "],"id":900},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"insert","lines":["n"]},{"start":{"row":86,"column":5},"end":{"row":86,"column":6},"action":"insert","lines":["u"]},{"start":{"row":86,"column":6},"end":{"row":86,"column":7},"action":"insert","lines":["m"]},{"start":{"row":86,"column":7},"end":{"row":86,"column":8},"action":"insert","lines":["e"]},{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"insert","lines":["r"]},{"start":{"row":86,"column":9},"end":{"row":86,"column":10},"action":"insert","lines":["o"]}],[{"start":{"row":86,"column":10},"end":{"row":86,"column":11},"action":"insert","lines":[" "],"id":901}],[{"start":{"row":86,"column":10},"end":{"row":86,"column":11},"action":"remove","lines":[" "],"id":902},{"start":{"row":86,"column":9},"end":{"row":86,"column":10},"action":"remove","lines":["o"]},{"start":{"row":86,"column":8},"end":{"row":86,"column":9},"action":"remove","lines":["r"]},{"start":{"row":86,"column":7},"end":{"row":86,"column":8},"action":"remove","lines":["e"]},{"start":{"row":86,"column":6},"end":{"row":86,"column":7},"action":"remove","lines":["m"]},{"start":{"row":86,"column":5},"end":{"row":86,"column":6},"action":"remove","lines":["u"]},{"start":{"row":86,"column":4},"end":{"row":86,"column":5},"action":"remove","lines":["n"]}],[{"start":{"row":86,"column":3},"end":{"row":86,"column":4},"action":"remove","lines":[" "],"id":903},{"start":{"row":86,"column":2},"end":{"row":86,"column":3},"action":"remove","lines":["r"]},{"start":{"row":86,"column":1},"end":{"row":86,"column":2},"action":"remove","lines":["o"]},{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"remove","lines":["f"]}],[{"start":{"row":4,"column":3},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":904},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["#"]},{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["r"]},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["n"],"id":905},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["g"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["o"]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":[" "],"id":906},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["i"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["n"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["i"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["c"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["i"]}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"remove","lines":["i"],"id":907},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"remove","lines":["c"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":["i"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"remove","lines":["n"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"remove","lines":["i"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"remove","lines":[" "]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"remove","lines":["o"]}],[{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["e"],"id":908}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":8},"action":"insert","lines":["()"],"id":909}],[{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["i"],"id":910},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["n"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["i"]},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["c"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["i"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["o"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":[","]}],[{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["f"],"id":911},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["i"]},{"start":{"row":5,"column":16},"end":{"row":5,"column":17},"action":"insert","lines":["n"]},{"start":{"row":5,"column":17},"end":{"row":5,"column":18},"action":"insert","lines":["a"]},{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["l"]}],[{"start":{"row":5,"column":20},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":912},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["#"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["r"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"remove","lines":["n"],"id":913}],[{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["a"],"id":914},{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["n"]},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["g"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":8},"action":"insert","lines":["()"],"id":915}],[{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["i"],"id":916},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["n"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["i"]},{"start":{"row":6,"column":10},"end":{"row":6,"column":11},"action":"insert","lines":["c"]},{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["i"]},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["o"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":[","]}],[{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":[" "],"id":917},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["f"]},{"start":{"row":6,"column":16},"end":{"row":6,"column":17},"action":"insert","lines":["i"]},{"start":{"row":6,"column":17},"end":{"row":6,"column":18},"action":"insert","lines":["n"]},{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["a"]},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["l"]}],[{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":[","],"id":918},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["s"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["s"]}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"remove","lines":["s"],"id":919}],[{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["a"],"id":920},{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":["l"]},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["t"]},{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":["o"]}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":[")"],"id":921},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["o"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["r"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["e"]},{"start":{"row":9,"column":19},"end":{"row":9,"column":20},"action":"remove","lines":["m"]},{"start":{"row":9,"column":18},"end":{"row":9,"column":19},"action":"remove","lines":["u"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"remove","lines":["n"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"remove","lines":["+"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"remove","lines":["a"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"remove","lines":["m"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"remove","lines":["u"]},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"remove","lines":["s"]},{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"remove","lines":["("]},{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"remove","lines":[" "]},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"remove","lines":["="]},{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"remove","lines":[" "]}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":[" "],"id":922},{"start":{"row":9,"column":9},"end":{"row":9,"column":10},"action":"insert","lines":["+"]}],[{"start":{"row":9,"column":10},"end":{"row":9,"column":11},"action":"insert","lines":["="],"id":923}],[{"start":{"row":9,"column":11},"end":{"row":9,"column":12},"action":"insert","lines":[" "],"id":924},{"start":{"row":9,"column":12},"end":{"row":9,"column":13},"action":"insert","lines":["n"]},{"start":{"row":9,"column":13},"end":{"row":9,"column":14},"action":"insert","lines":["u"]},{"start":{"row":9,"column":14},"end":{"row":9,"column":15},"action":"insert","lines":["m"]},{"start":{"row":9,"column":15},"end":{"row":9,"column":16},"action":"insert","lines":["e"]},{"start":{"row":9,"column":16},"end":{"row":9,"column":17},"action":"insert","lines":["r"]},{"start":{"row":9,"column":17},"end":{"row":9,"column":18},"action":"insert","lines":["o"]}],[{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"insert","lines":["h"],"id":925},{"start":{"row":53,"column":1},"end":{"row":53,"column":2},"action":"insert","lines":["i"]}],[{"start":{"row":53,"column":1},"end":{"row":53,"column":2},"action":"remove","lines":["i"],"id":926},{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"remove","lines":["h"]},{"start":{"row":52,"column":0},"end":{"row":53,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":52,"column":0},"end":{"row":52,"column":1},"action":"insert","lines":["c"],"id":927},{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"insert","lines":["o"]},{"start":{"row":52,"column":2},"end":{"row":52,"column":3},"action":"insert","lines":["n"]},{"start":{"row":52,"column":3},"end":{"row":52,"column":4},"action":"insert","lines":["t"]},{"start":{"row":52,"column":4},"end":{"row":52,"column":5},"action":"insert","lines":["a"]},{"start":{"row":52,"column":5},"end":{"row":52,"column":6},"action":"insert","lines":["d"]},{"start":{"row":52,"column":6},"end":{"row":52,"column":7},"action":"insert","lines":["o"]},{"start":{"row":52,"column":7},"end":{"row":52,"column":8},"action":"insert","lines":["r"]}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"insert","lines":[" "],"id":928},{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"insert","lines":["="]}],[{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"insert","lines":[" "],"id":929},{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"insert","lines":["1"]}],[{"start":{"row":52,"column":12},"end":{"row":53,"column":0},"action":"insert","lines":["",""],"id":930},{"start":{"row":53,"column":0},"end":{"row":54,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":87,"column":40},"end":{"row":88,"column":0},"action":"insert","lines":["",""],"id":931},{"start":{"row":88,"column":0},"end":{"row":89,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"insert","lines":["f"],"id":932},{"start":{"row":89,"column":1},"end":{"row":89,"column":2},"action":"insert","lines":["o"]},{"start":{"row":89,"column":2},"end":{"row":89,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":89,"column":3},"end":{"row":89,"column":4},"action":"insert","lines":[" "],"id":933}],[{"start":{"row":89,"column":4},"end":{"row":89,"column":5},"action":"insert","lines":["n"],"id":934},{"start":{"row":89,"column":5},"end":{"row":89,"column":6},"action":"insert","lines":["u"]},{"start":{"row":89,"column":6},"end":{"row":89,"column":7},"action":"insert","lines":["m"]},{"start":{"row":89,"column":7},"end":{"row":89,"column":8},"action":"insert","lines":["e"]},{"start":{"row":89,"column":8},"end":{"row":89,"column":9},"action":"insert","lines":["r"]},{"start":{"row":89,"column":9},"end":{"row":89,"column":10},"action":"insert","lines":["o"]}],[{"start":{"row":89,"column":10},"end":{"row":89,"column":11},"action":"insert","lines":[" "],"id":935}],[{"start":{"row":89,"column":10},"end":{"row":89,"column":11},"action":"remove","lines":[" "],"id":936},{"start":{"row":89,"column":9},"end":{"row":89,"column":10},"action":"remove","lines":["o"]},{"start":{"row":89,"column":8},"end":{"row":89,"column":9},"action":"remove","lines":["r"]},{"start":{"row":89,"column":7},"end":{"row":89,"column":8},"action":"remove","lines":["e"]},{"start":{"row":89,"column":6},"end":{"row":89,"column":7},"action":"remove","lines":["m"]},{"start":{"row":89,"column":5},"end":{"row":89,"column":6},"action":"remove","lines":["u"]},{"start":{"row":89,"column":4},"end":{"row":89,"column":5},"action":"remove","lines":["n"]}],[{"start":{"row":89,"column":4},"end":{"row":89,"column":5},"action":"insert","lines":["x"],"id":937}],[{"start":{"row":89,"column":5},"end":{"row":89,"column":6},"action":"insert","lines":[" "],"id":938},{"start":{"row":89,"column":6},"end":{"row":89,"column":7},"action":"insert","lines":["i"]},{"start":{"row":89,"column":7},"end":{"row":89,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":89,"column":8},"end":{"row":89,"column":9},"action":"insert","lines":[" "],"id":939},{"start":{"row":89,"column":9},"end":{"row":89,"column":10},"action":"insert","lines":["r"]},{"start":{"row":89,"column":10},"end":{"row":89,"column":11},"action":"insert","lines":["a"]},{"start":{"row":89,"column":11},"end":{"row":89,"column":12},"action":"insert","lines":["n"]},{"start":{"row":89,"column":12},"end":{"row":89,"column":13},"action":"insert","lines":["g"]},{"start":{"row":89,"column":13},"end":{"row":89,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":89,"column":14},"end":{"row":89,"column":16},"action":"insert","lines":["()"],"id":940}],[{"start":{"row":89,"column":15},"end":{"row":89,"column":16},"action":"insert","lines":["n"],"id":941},{"start":{"row":89,"column":16},"end":{"row":89,"column":17},"action":"insert","lines":["u"]},{"start":{"row":89,"column":17},"end":{"row":89,"column":18},"action":"insert","lines":["m"]},{"start":{"row":89,"column":18},"end":{"row":89,"column":19},"action":"insert","lines":["e"]},{"start":{"row":89,"column":19},"end":{"row":89,"column":20},"action":"insert","lines":["r"]},{"start":{"row":89,"column":20},"end":{"row":89,"column":21},"action":"insert","lines":["o"]}],[{"start":{"row":89,"column":20},"end":{"row":89,"column":21},"action":"remove","lines":["o"],"id":942},{"start":{"row":89,"column":19},"end":{"row":89,"column":20},"action":"remove","lines":["r"]},{"start":{"row":89,"column":18},"end":{"row":89,"column":19},"action":"remove","lines":["e"]},{"start":{"row":89,"column":17},"end":{"row":89,"column":18},"action":"remove","lines":["m"]},{"start":{"row":89,"column":16},"end":{"row":89,"column":17},"action":"remove","lines":["u"]},{"start":{"row":89,"column":15},"end":{"row":89,"column":16},"action":"remove","lines":["n"]}],[{"start":{"row":89,"column":15},"end":{"row":89,"column":16},"action":"insert","lines":["1"],"id":943},{"start":{"row":89,"column":16},"end":{"row":89,"column":17},"action":"insert","lines":[","]}],[{"start":{"row":89,"column":17},"end":{"row":89,"column":18},"action":"insert","lines":[" "],"id":944},{"start":{"row":89,"column":18},"end":{"row":89,"column":19},"action":"insert","lines":["n"]},{"start":{"row":89,"column":19},"end":{"row":89,"column":20},"action":"insert","lines":["u"]},{"start":{"row":89,"column":20},"end":{"row":89,"column":21},"action":"insert","lines":["m"]},{"start":{"row":89,"column":21},"end":{"row":89,"column":22},"action":"insert","lines":["e"]},{"start":{"row":89,"column":22},"end":{"row":89,"column":23},"action":"insert","lines":["r"]},{"start":{"row":89,"column":23},"end":{"row":89,"column":24},"action":"insert","lines":["o"]}],[{"start":{"row":89,"column":24},"end":{"row":89,"column":25},"action":"insert","lines":["+"],"id":945},{"start":{"row":89,"column":25},"end":{"row":89,"column":26},"action":"insert","lines":["1"]}],[{"start":{"row":89,"column":27},"end":{"row":89,"column":28},"action":"insert","lines":[":"],"id":946}],[{"start":{"row":89,"column":28},"end":{"row":90,"column":0},"action":"insert","lines":["",""],"id":947},{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "]},{"start":{"row":90,"column":4},"end":{"row":90,"column":5},"action":"insert","lines":["p"]},{"start":{"row":90,"column":5},"end":{"row":90,"column":6},"action":"insert","lines":["r"]},{"start":{"row":90,"column":6},"end":{"row":90,"column":7},"action":"insert","lines":["i"]},{"start":{"row":90,"column":7},"end":{"row":90,"column":8},"action":"insert","lines":["n"]},{"start":{"row":90,"column":8},"end":{"row":90,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":90,"column":9},"end":{"row":90,"column":11},"action":"insert","lines":["()"],"id":948}],[{"start":{"row":90,"column":10},"end":{"row":90,"column":12},"action":"insert","lines":["\"\""],"id":949}],[{"start":{"row":90,"column":10},"end":{"row":90,"column":12},"action":"remove","lines":["\"\""],"id":950}],[{"start":{"row":90,"column":10},"end":{"row":90,"column":11},"action":"insert","lines":["x"],"id":951}],[{"start":{"row":52,"column":12},"end":{"row":53,"column":0},"action":"insert","lines":["",""],"id":952},{"start":{"row":53,"column":0},"end":{"row":54,"column":0},"action":"insert","lines":["",""]},{"start":{"row":54,"column":0},"end":{"row":54,"column":1},"action":"insert","lines":["w"]},{"start":{"row":54,"column":1},"end":{"row":54,"column":2},"action":"insert","lines":["h"]},{"start":{"row":54,"column":2},"end":{"row":54,"column":3},"action":"insert","lines":["i"]}],[{"start":{"row":54,"column":3},"end":{"row":54,"column":4},"action":"insert","lines":["l"],"id":953},{"start":{"row":54,"column":4},"end":{"row":54,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":54,"column":5},"end":{"row":54,"column":6},"action":"insert","lines":[" "],"id":954}],[{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"insert","lines":["c"],"id":955},{"start":{"row":54,"column":7},"end":{"row":54,"column":8},"action":"insert","lines":["o"]},{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"insert","lines":["n"]},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":["t"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["a"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["d"]},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["o"]},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":[" "],"id":956}],[{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"remove","lines":[" "],"id":957},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"remove","lines":["r"]},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"remove","lines":["o"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"remove","lines":["d"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"remove","lines":["a"]},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"remove","lines":["t"]},{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"remove","lines":["n"]},{"start":{"row":54,"column":7},"end":{"row":54,"column":8},"action":"remove","lines":["o"]},{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"remove","lines":["c"]}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":6},"action":"remove","lines":["while "],"id":958}],[{"start":{"row":54,"column":0},"end":{"row":54,"column":1},"action":"insert","lines":["w"],"id":959},{"start":{"row":54,"column":1},"end":{"row":54,"column":2},"action":"insert","lines":["h"]},{"start":{"row":54,"column":2},"end":{"row":54,"column":3},"action":"insert","lines":["i"]},{"start":{"row":54,"column":3},"end":{"row":54,"column":4},"action":"insert","lines":["l"]},{"start":{"row":54,"column":4},"end":{"row":54,"column":5},"action":"insert","lines":["e"]}],[{"start":{"row":54,"column":5},"end":{"row":54,"column":6},"action":"insert","lines":[" "],"id":960},{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"insert","lines":["c"]},{"start":{"row":54,"column":7},"end":{"row":54,"column":8},"action":"insert","lines":["o"]},{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"insert","lines":["n"]},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":["t"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["a"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["d"]},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["o"]},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["r"]}],[{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":["+"],"id":961},{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["+"]}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"remove","lines":["+"],"id":962}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["="],"id":963}],[{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":[" "],"id":964}],[{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"remove","lines":[" "],"id":965}],[{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":[" "],"id":966}],[{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"remove","lines":[" "],"id":967}],[{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":[":"],"id":968}],[{"start":{"row":54,"column":17},"end":{"row":55,"column":0},"action":"insert","lines":["",""],"id":969},{"start":{"row":55,"column":0},"end":{"row":55,"column":4},"action":"insert","lines":["    "]},{"start":{"row":55,"column":4},"end":{"row":55,"column":5},"action":"insert","lines":["p"]},{"start":{"row":55,"column":5},"end":{"row":55,"column":6},"action":"insert","lines":["r"]},{"start":{"row":55,"column":6},"end":{"row":55,"column":7},"action":"insert","lines":["i"]}],[{"start":{"row":55,"column":7},"end":{"row":55,"column":8},"action":"insert","lines":["n"],"id":970},{"start":{"row":55,"column":8},"end":{"row":55,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":55,"column":9},"end":{"row":55,"column":11},"action":"insert","lines":["()"],"id":971}],[{"start":{"row":55,"column":10},"end":{"row":55,"column":11},"action":"insert","lines":["c"],"id":972},{"start":{"row":55,"column":11},"end":{"row":55,"column":12},"action":"insert","lines":["o"]},{"start":{"row":55,"column":12},"end":{"row":55,"column":13},"action":"insert","lines":["n"]},{"start":{"row":55,"column":13},"end":{"row":55,"column":14},"action":"insert","lines":["t"]},{"start":{"row":55,"column":14},"end":{"row":55,"column":15},"action":"insert","lines":["a"]},{"start":{"row":55,"column":15},"end":{"row":55,"column":16},"action":"insert","lines":["d"]},{"start":{"row":55,"column":16},"end":{"row":55,"column":17},"action":"insert","lines":["o"]},{"start":{"row":55,"column":17},"end":{"row":55,"column":18},"action":"insert","lines":["r"]}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"remove","lines":["="],"id":973},{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"remove","lines":["+"]}],[{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":["+"],"id":974},{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["1"]}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"remove","lines":["1"],"id":975},{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"remove","lines":["+"]},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"remove","lines":["r"]},{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"remove","lines":["o"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"remove","lines":["d"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"remove","lines":["a"]},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"remove","lines":["t"]},{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"remove","lines":["n"]},{"start":{"row":54,"column":7},"end":{"row":54,"column":8},"action":"remove","lines":["o"]},{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"remove","lines":["c"]}],[{"start":{"row":54,"column":6},"end":{"row":54,"column":7},"action":"insert","lines":["o"],"id":976},{"start":{"row":54,"column":7},"end":{"row":54,"column":8},"action":"insert","lines":["p"]},{"start":{"row":54,"column":8},"end":{"row":54,"column":9},"action":"insert","lines":["c"]},{"start":{"row":54,"column":9},"end":{"row":54,"column":10},"action":"insert","lines":["i"]},{"start":{"row":54,"column":10},"end":{"row":54,"column":11},"action":"insert","lines":["o"]},{"start":{"row":54,"column":11},"end":{"row":54,"column":12},"action":"insert","lines":["n"]}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":[" "],"id":977}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"remove","lines":[" "],"id":978}],[{"start":{"row":54,"column":12},"end":{"row":54,"column":13},"action":"insert","lines":["_"],"id":979},{"start":{"row":54,"column":13},"end":{"row":54,"column":14},"action":"insert","lines":["u"]},{"start":{"row":54,"column":14},"end":{"row":54,"column":15},"action":"insert","lines":["s"]},{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["a"]},{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":["r"]},{"start":{"row":54,"column":17},"end":{"row":54,"column":18},"action":"insert","lines":["i"]},{"start":{"row":54,"column":18},"end":{"row":54,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":54,"column":18},"end":{"row":54,"column":19},"action":"remove","lines":["o"],"id":980},{"start":{"row":54,"column":17},"end":{"row":54,"column":18},"action":"remove","lines":["i"]},{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"remove","lines":["r"]},{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"remove","lines":["a"]}],[{"start":{"row":54,"column":15},"end":{"row":54,"column":16},"action":"insert","lines":["u"],"id":981},{"start":{"row":54,"column":16},"end":{"row":54,"column":17},"action":"insert","lines":["a"]},{"start":{"row":54,"column":17},"end":{"row":54,"column":18},"action":"insert","lines":["r"]},{"start":{"row":54,"column":18},"end":{"row":54,"column":19},"action":"insert","lines":["i"]},{"start":{"row":54,"column":19},"end":{"row":54,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":54,"column":20},"end":{"row":54,"column":21},"action":"insert","lines":[" "],"id":982},{"start":{"row":54,"column":21},"end":{"row":54,"column":22},"action":"insert","lines":["="]},{"start":{"row":54,"column":22},"end":{"row":54,"column":23},"action":"insert","lines":["!"]}],[{"start":{"row":54,"column":23},"end":{"row":54,"column":24},"action":"insert","lines":[" "],"id":983}],[{"start":{"row":54,"column":24},"end":{"row":54,"column":25},"action":"insert","lines":["\""],"id":984},{"start":{"row":54,"column":25},"end":{"row":54,"column":26},"action":"insert","lines":["s"]},{"start":{"row":54,"column":26},"end":{"row":54,"column":27},"action":"insert","lines":["t"]},{"start":{"row":54,"column":27},"end":{"row":54,"column":28},"action":"insert","lines":["o"]},{"start":{"row":54,"column":28},"end":{"row":54,"column":29},"action":"insert","lines":["p"]},{"start":{"row":54,"column":29},"end":{"row":54,"column":30},"action":"insert","lines":["\""]}],[{"start":{"row":53,"column":0},"end":{"row":53,"column":1},"action":"insert","lines":["o"],"id":985},{"start":{"row":53,"column":1},"end":{"row":53,"column":2},"action":"insert","lines":["p"]},{"start":{"row":53,"column":2},"end":{"row":53,"column":3},"action":"insert","lines":["c"]},{"start":{"row":53,"column":3},"end":{"row":53,"column":4},"action":"insert","lines":["i"]},{"start":{"row":53,"column":4},"end":{"row":53,"column":5},"action":"insert","lines":["o"]},{"start":{"row":53,"column":5},"end":{"row":53,"column":6},"action":"insert","lines":["n"]},{"start":{"row":53,"column":6},"end":{"row":53,"column":7},"action":"insert","lines":["_"]},{"start":{"row":53,"column":7},"end":{"row":53,"column":8},"action":"insert","lines":["u"]},{"start":{"row":53,"column":8},"end":{"row":53,"column":9},"action":"insert","lines":["s"]}],[{"start":{"row":53,"column":9},"end":{"row":53,"column":10},"action":"insert","lines":["u"],"id":986},{"start":{"row":53,"column":10},"end":{"row":53,"column":11},"action":"insert","lines":["a"]},{"start":{"row":53,"column":11},"end":{"row":53,"column":12},"action":"insert","lines":["r"]},{"start":{"row":53,"column":12},"end":{"row":53,"column":13},"action":"insert","lines":["i"]},{"start":{"row":53,"column":13},"end":{"row":53,"column":14},"action":"insert","lines":["o"]}],[{"start":{"row":53,"column":14},"end":{"row":53,"column":15},"action":"insert","lines":[" "],"id":987},{"start":{"row":53,"column":15},"end":{"row":53,"column":16},"action":"insert","lines":["="]}],[{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"insert","lines":[" "],"id":988}],[{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"remove","lines":[" "],"id":989}],[{"start":{"row":53,"column":16},"end":{"row":53,"column":17},"action":"insert","lines":[" "],"id":990}],[{"start":{"row":53,"column":17},"end":{"row":53,"column":19},"action":"insert","lines":["\"\""],"id":991}]]},"ace":{"folds":[],"scrolltop":480,"scrollleft":0,"selection":{"start":{"row":58,"column":0},"end":{"row":58,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":31,"state":"start","mode":"ace/mode/python"}},"timestamp":1732810528999}