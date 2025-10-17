"""
Demostración del Principio de Inversión de Dependencias (DIP)
versión adaptada para una televisión controlada por un mando (control remoto).
Solo se incluye la parte que aplica DIP (sin la sección "sin DIP").
"""

from abc import ABC, abstractmethod

# Abstracción: dispositivo de control (ej. un mando)
class RemoteControl(ABC):
	@abstractmethod
	def power_on(self):
		pass
	@abstractmethod
	def power_off(self):
		pass

# Implementación concreta del control remoto
class TvRemote(RemoteControl):
	def power_on(self):
		print("Enciende la televisión")
	def power_off(self):
		print("Apaga la televisión")

# Televisión depende de la abstracción RemoteControl
class Television:
	def __init__(self, remote: RemoteControl) -> None:
		self.remote = remote
	def operate(self, command):
		if command == "ON":
			self.remote.power_on()
		elif command == "OFF":
			self.remote.power_off()

# Prueba breve (inyección de dependencia)
tv = Television(TvRemote())
tv.operate("ON")
tv.operate("OFF")

