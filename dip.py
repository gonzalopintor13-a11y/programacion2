"""
Demostración del Principio de Inversión de Dependencias (DIP)
en el contexto de una lámpara controlada por un interruptor.
"""

# Sin DIP
from abc import ABC, abstractmethod

class Switch:
    def turn_on(self):
        print("Enciende la luz")
    def turn_off(self):
        print("Apaga la luz")

class Lamp:
    def __init__(self) -> None:
        self.switch = Switch()
    def operate(self, command):
        if command == "ON":
            self.switch.turn_on()
        elif command == "OFF":
            self.switch.turn_off()

# Prueba sin DIP
lamp = Lamp()
lamp.operate("ON")
lamp.operate("OFF")

#---------------------------------------------------------------------------------------#

# Con DIP
'''
Sin DIP: `Lamp` depende de la clase concreta `Switch` (acoplamiento fuerte).
Con DIP: `Lamp` depende de la abstracción `AbstractSwitch` y recibe la
implementación por inyección, lo que reduce acoplamiento y mejora tests.
'''
class AbstractSwitch(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass

class LampSwitch(AbstractSwitch):
    # Implementación concreta del interruptor (breve).
    def turn_on(self):
        print("Enciende la luz")
    def turn_off(self):
        print("Apaga la luz")

class Lamp:
    # Lamp recibe una implementación de `AbstractSwitch` (inyección).
    # Ventajas: desacoplamiento, testabilidad y flexibilidad.
    def __init__(self, switch: AbstractSwitch) -> None:
        self.switch = switch
    def operate(self, command):
        if command == "ON":
            self.switch.turn_on()
        elif command == "OFF":
            self.switch.turn_off()

# Prueba con DIP (concisa): inyectamos `LampSwitch` en `Lamp`.
lamp = Lamp(LampSwitch())
lamp.operate("ON")
lamp.operate("OFF")


