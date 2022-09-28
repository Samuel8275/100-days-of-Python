""" class Taza():
    color = "blanco"
    mensaje = None
    material = "porcelana"
    limpia = True

taza_1 = Taza()
taza_2 = Taza()

print(taza_1)
print(taza_2)
print(taza_1.color)
print(taza_2.color)
taza_2.color = "green"
print(taza_2.color) """

""" class Vehiculo():
    color = None
    longitud_metros = None
    ruedas = 4

    def arrancar(self):
        print("El vehiculo a arrancado.")

    def detener(self):
        print("El vehiculo esta detenido.")

vehiculo_1 = Vehiculo()
vehiculo_2 = Vehiculo()
vehiculo_2.material_aleron = "Fibra de carbono"
print(vehiculo_2.material_aleron)
vehiculo_1.arrancar()
vehiculo_1.detener() """


""" class Vehiculo():

    pais_origen = "Alemania"

    def __init__(self, color, longitud_metros, ruedas):
        self.color = color
        self.longitud_metros = longitud_metros
        self.ruedas = ruedas

    def arrancar(self):
        print("El vehiculo a arrancado.")

    def detener(self):
        print("El vehiculo esta detenido.")

    def mostrar_info(self):
        print(f"El vehiculo es de color {self.color}, tiene {self.ruedas} ruedas y mide {self.longitud_metros}m de largo.")

vehiculo1 = Vehiculo("rojo", 4, 4)
vehiculo2 = Vehiculo("azul", 6, 8)
print(vehiculo1.pais_origen)
vehiculo1.mostrar_info()
vehiculo2.mostrar_info() """

""" class Vehiculo():
    pass """

    
