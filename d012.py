# Proyecto

class Motocicleta():
    estado = "nueva"
    motor = False

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso, combustible_maximo):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.combustible_maximo = combustible_maximo

    def arrancar(self):
        if self.motor == False:
            print("EL motor ha arrancado");
            self.motor = True;
        elif self.motor == True:
            print("EL motor ya estava en marcha");
        else:
            print("Error");

    def detener(self):
        if self.motor == False:
            print("El motor ya estava detenido");
        elif self.motor == True:
            print("El motor se a detenido");
            self.motor = False;
        else:
            print("Error");
        
    def consulta_precio(self):
        print(f"El precio de la motocicleta {self.marca} modelo {self.modelo} es de {self.precio}€");
    
    def repostar(self):
        while True:
            self.repostar_litros = float(input("Por favor, introduzca la cantidad de litros que desea repostar:\n"));
            
            if self.combustible_litros + self.repostar_litros <= self.combustible_maximo:
                print("Repostaje exitoso.");
                print(f"Se han repostado {self.repostar_litros} litros.");
                self.combustible_litros += self.repostar_litros 
                print(f"El depósito tiene {self.combustible_litros} litros de combustible.");
                break
            else:
                print("No cabe tanto combustible. ¿Quieres encharcar el concesionario?");


Motocicleta1 = Motocicleta("roja", "3456HFSD", 10, 2, "Yamaha", "GT450", "3-11-2005", 200, 250, 20);
Motocicleta2 = Motocicleta(combustible_litros=0, color="blanca", marca="BMW", modelo="RTX3090", numero_ruedas=3, matricula="9432-HSOA", fecha_fabricacion="25-03-2006", velocidad_punta=220, peso=300, combustible_maximo=30);

Motocicleta1.arrancar();
Motocicleta1.arrancar();
Motocicleta2.detener();

Motocicleta2.precio = 12000;

Motocicleta2.consulta_precio()
Motocicleta1.repostar();


