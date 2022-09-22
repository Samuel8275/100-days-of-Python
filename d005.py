""" for i in range(5, 11, 2):
    print(f"I es igual a: {i}") """

""" colors = ["rojo", "azul", "verde", "amarillo"]
print("--Listado de colores--")

for color in colors:
    if color == "azul" or color == "verde":
        print("Este color esta censurado")
        continue
    else:
        print(color) """

""" colors = ["rojo", "azul", "verde", "amarillo"]
print("--Listado de colores--")

for color in colors:
    if color == "azul":
        print("Se a roto la ejecucion")
        break
    else:
        print(color) """

""" i = 1

while i <= 10:
    print(i)
    i += 1 """

""" while True:
    salida = input("Escriba literalmente salida para salir: ").lower()
    if salida == "salir":
        break """

# Ejercicios

""" for i in range(7, 15):
    print(f"El valor del bucle es: {i}")


i = 7
while i <= 14:
    print(f"El valor del bucle es: {i}")
    i += 1 """

""" for i in range(0, -5500, -500):
    print(f"El valor del bucle es: {i}")


i = 0
while i >= -5000:
    print(f"El valor del bucle es: {i}")
    i -= 500 """


""" colores = ["verde", "rosa", "amarillo", "negro", "blanco", "rojo", "marron"]

for color in colores:
    print(color) """

""" numeros = [10, 45, 356, 10, 10, 10, 46, 67, 45, 10, 10, 43,10, 65,10,10]

numeros.sort()

for numero in numeros:
    if numero == 10:
        continue
    if numero == 356:
        break
    print(f"Numero: {numero}") """

# Proyecto:

print("-> Pizzeria Samuel <-")
dinero = int(input("De cuanto dinero dispone: "))
pizzas = []
print("Introduzca el numero de la Pizza que quiere")
pizza_cliente = input("1- Margarita 2- Peperoni 3- BBQ:\n")

if pizza_cliente == "1":

    precio = 20
    cambio = dinero - precio
    pizzas.append("margarita")
    print(f"Pizza {pizzas[0]} seleccionada")
    print(f"El precio del pedido actual es de {precio}€")

    if cambio > 0:
        print(f"Le quedan {cambio}€")
        extra = input("Desea ingredientes extra?\n1- Yes\n2-No\n")

        while extra == "1":
            print("Introduzca el numero del ingrediente que quiere")
            pizza_ingredientes = input("1- Picante 2- Queso 3- Oregano:\n")

            if pizza_ingredientes == "1":
                precio_ingrediente = 3
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido picante a la pizza.")
                print(f"El precio del picante es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")

            elif pizza_ingredientes == "2":
                precio_ingrediente = 5
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido queso a la pizza.")
                print(f"El precio del queso es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")

            elif pizza_ingredientes == "3":
                precio_ingrediente = 4
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido oregano a la pizza.")
                print(f"El precio del oregano es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")
            
        if extra == "2":
            print(f"Su pedido a sido terminado.")

    elif cambio == 0:
        print("no le queda mas dinero para ingredientes extra.")
    else:
        print("No tiene dinero suficiente vuelvalo a intentar")
        exit()

elif pizza_cliente == "2":
    precio = 25
    cambio = dinero - precio
    pizzas.append("peperoni")
    print(f"Pizza {pizzas[0]} seleccionada")
    print(f"El precio del pedido actual es de {precio}€")

    if cambio > 0:
        print(f"Le quedan {cambio}€")
        extra = input("Desea ingredientes extra?\n1- Yes\n2-No\n")

        while extra == "1":
            print("Introduzca el numero del ingrediente que quiere")
            pizza_ingredientes = input("1- Picante 2- Queso 3- Oregano:\n")

            if pizza_ingredientes == "1":
                precio_ingrediente = 3
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido picante a la pizza.")
                print(f"El precio del picante es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")

            elif pizza_ingredientes == "2":
                precio_ingrediente = 5
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido queso a la pizza.")
                print(f"El precio del queso es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")

            elif pizza_ingredientes == "3":
                precio_ingrediente = 4
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido oregano a la pizza.")
                print(f"El precio del oregano es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")
            
        if extra == "2":
            print(f"Su pedido a sido terminado.")

    elif cambio == 0:
        print("no le queda mas dinero para ingredientes extra.")

    else:
        print("No tiene dinero suficiente vuelvalo a intentar")
        exit()

elif pizza_cliente == "3":
    precio = 30
    cambio = dinero - precio
    pizzas.append("BBQ")
    print(f"Pizza {pizzas[0]} seleccionada")
    print(f"El precio del pedido actual es de {precio}€")

    if cambio > 0:
        print(f"Le quedan {cambio}€")
        extra = input("Desea ingredientes extra?\n1- Yes\n2-No\n")

        while extra == "1":
            print("Introduzca el numero del ingrediente que quiere")
            pizza_ingredientes = input("1- Picante 2- Queso 3- Oregano:\n")

            if pizza_ingredientes == "1":
                precio_ingrediente = 3
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido picante a la pizza.")
                print(f"El precio del picante es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")

            elif pizza_ingredientes == "2":
                precio_ingrediente = 5
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido queso a la pizza.")
                print(f"El precio del queso es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")

            elif pizza_ingredientes == "3":
                precio_ingrediente = 4
                precio = precio + precio_ingrediente
                cambio = cambio - precio_ingrediente
                print("Se le a añadido oregano a la pizza.")
                print(f"El precio del oregano es de {precio_ingrediente}€")
                print(f"El precio actual es de {precio}€ y el cambio de {cambio}")
                if cambio == 0 or cambio < 0:
                    print("No le queda mas dinero asi que su pedido a terminado")
                    exit()
                extra = input("Desea más ingredientes extra?\n1-Yes\n2-No\n")
            
        if extra == "2":
            print(f"Su pedido a sido terminado.")

    elif cambio == 0:
        print("no le queda mas dinero para ingredientes extra.")

    else:
        print("No tiene dinero suficiente vuelvalo a intentar")
        exit()

else:
    print("Error")

