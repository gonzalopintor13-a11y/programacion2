'''
SOLID - Principio de Sustitución de Liskov (LSP)

Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como cumplir el LSP.
 Instrucciones:
 1. Crea la clase Vehículo.
 2. Añade tres subclases de Vehículo.
 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 4. Desarrolla un código que compruebe que se cumple el LSP.
'''

# Clase padre

class Vehicle:
    def __init__(self, speed=0):
        self.speed = speed

    def accelerate(self, increment):
        self.speed += increment
        print(f"Velocidad: {self.speed} km/h")

    def brake(self, decrement):
        self.speed -= decrement
        if self.speed <= 0:
            self.speed = 0
        print(f"Velocidad: {self.speed} km/h")


#Subclases

class Coche(Vehicle):
    def accelerate(self, increment):
        print("Acelerando el coche...")
        super().accelerate(increment)

    def brake(self, decrement):
        print("Frenando el coche...")
        super().brake(decrement)

class Bicicleta(Vehicle):
    def accelerate(self, increment):
        print("Pedaleando la bicicleta...")
        super().accelerate(increment)

    def brake(self, decrement):
        print("Frenando la bicicleta...")
        super().brake(decrement)

class Avion(Vehicle):
    def accelerate(self, increment):
        print("Acelerando el avión...")
        super().accelerate(increment)

    def brake(self, decrement):
        print("Frenando el avión...")
        super().brake(decrement)

# Función para probar el LSP

def test_vehicle(vehicle):
    vehicle.accelerate(50)
    vehicle.brake(20)

# Pruebas
coche = Coche()
bicicleta = Bicicleta()
avion = Avion() 
test_vehicle(coche)
test_vehicle(bicicleta)   
test_vehicle(avion)