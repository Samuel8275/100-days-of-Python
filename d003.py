""" numero = 10

if numero > 7:
    print("El numero es mayor que 7")
elif numero == 7:
    print("El numero es igual a 7")
else:
    print("El numero es menor que 7") """

""" edad = int(input("Introduzca su edad:\n"))
respuesta = None

if edad >= 18:
    print("Es mayor de edad puede pasar a la discoteca. Introduzca la entrada que tenga: ")
    respuesta = input("1- Normal. \n2- Golden. \n3- VIP\n")
    
    if respuesta == "1":
        print("Tiene una entrada Normal.")
    elif respuesta == "2":
        print("Tiene una entrada Golden.")
    elif respuesta == "3":
        print("Tiene una entrada VIP.")
    else:
        print("Respuesta no valida.")
else:
    print("Lo sentimos pero es menor de edad y no puede entrar a la discoteca.") """

""" color = "rojo"
forma = "circulo"
tamaño = "grande"

if color == "rojo" and forma == "circulo" and tamaño == "grande":
    print("es un circulo rojo y grande.")
else:
    print("no es un circulo rojo")

if color == "rojo" or forma == "cuadrado":
    print("La condicion se cumple")

if not(color == "azul" and forma == "cuadrado"):
    print("El color no es azul ni es un cuadrado.") """

""" error = input("Introduzca un codigo de error: \n")

match error:
    case "200":
        print("All okay")
    case "301":
        print("Error 301")
    case _:
        print("Error no disponible") """

# Ejercicios:

# Los ejercicios los e hecho mirando el video pausandolo y respondiendo.

# Proyecto:

""" num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))
print("Inserte un numero que corresponda a la operacion que desea realizar: ")
operacion = input("1- suma:\n2- resta:\n3- multiplicacion:\n4- division:\n5- exponentes:\n")

if operacion == "1":
    suma = num1 + num2
    print(f"El resultado es: {suma}" )
elif operacion == "2":
    resta = num1 - num2
    print(f"El resultado es: {resta}")
elif operacion == "3":
    multiplicacion = num1 * num2
    print(f"El resultado es:  {multiplicacion}")
elif operacion == "4":
    division = num1 // num2
    resto = num1 % num2
    print(f"El resultado de la division es: {division}")
    if resto == 0:
        print("La division no tiene resto")
    else:
        print(f"El resto de la division es: {resto}")
elif operacion == "5":
    exponente = num1**num2
    print(f"El resultado de {num1} elevado a {num2} es: {exponente}")
else:
    print("Algo a fallado") """
