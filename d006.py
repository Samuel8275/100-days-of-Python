""" def saludar():
    nombre = input("Introduzca su nombre porfavor: ")
    print(f"Hola, {nombre}")

saludar() """

""" def saludar(nombre, edad):
    print(f"Hola, {nombre}")
    print(f"Usted tiene {edad} años.")

saludar("Samuel", 18) """

""" def suma(num1, num2):
    return num1 + num2

resultado1 = suma(3, 8)
resultado2 = suma(2, 2)
suma_sumas = resultado1 + resultado2

print(suma_sumas) """

# Ejercicios:

""" colores = ["rojo", "verde", "amarillo"]
def add_color():
    color = input("Que color quieres añadir? ")
    colores.insert(0, color)
add_color()
print(colores) """

# Proyecto:

""" num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))
print("Inserte un numero que corresponda a la operacion que desea realizar: \n")
operacion = input("1- suma:\n2- resta:\n3- multiplicacion:\n4- division:\n5- exponentes:\n")

def sumar(num1, num2):
    suma = num1 + num2
    print(f"El resultado es: {suma}")

def restar(num1, num2):
    resta = num1 - num2
    print(f"El resultado es: {resta}")

def multiplicar(num1, num2):
    multiplicacion = num1 * num2
    print(f"El resultado es: {multiplicacion}")

def dividir(num1, num2):
    division = num1 // num2
    resto = num1 % num2
    print(f"El resultado es: {division} y el resto {resto}")

def potenciar(num1, num2):
    potencia = num1**num2
    print(f"{num1} elevado a {num2} es: {potencia}")

repetir = input("Quieres operar?\n1-Yes\n2-No\n")

while repetir == "1" or repetir == "Yes":
    if operacion == "1":
        sumar(num1, num2)
    elif operacion == "2":
        restar(num1, num2)
    elif operacion == "3":
        multiplicar(num1, num2)
    elif operacion == "4":
        dividir(num1, num2)
    elif operacion == "5":
        potenciar(num1, num2)
    else:
        print("Algo a fallado")
    repetir = input("Quieres hacer otra operacion?\n1-Yes\n2-No\n")
    if repetir == "1" or repetir == "Yes":
        num1 = int(input("Introduzca el primer numero: "))
        num2 = int(input("Introduzca el segundo numero: "))
        print("Inserte un numero que corresponda a la operacion que desea realizar: \n")
        operacion = input("1- suma:\n2- resta:\n3- multiplicacion:\n4- division:\n5- exponentes:\n")

print("ADIOS") """