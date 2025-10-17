from abc import ABC, abstractmethod

"""
Demostración del Principio de Inversión de Dependencias (DIP)
Sistema de notificaciones (Email, SMS, PUSH)
"""

# Interfaz / Abstracción
class NotificationSender(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

# Implementaciones específicas
class EmailSender(NotificationSender):
    def send(self, message, recipient):
        print(f"Enviando Email a {recipient}: {message}")

class SMSSender(NotificationSender):
    def send(self, message, recipient):
        print(f"Enviando SMS a {recipient}: {message}")

class PushSender(NotificationSender):
    def send(self, message, recipient):
        print(f"Enviando notificación PUSH a {recipient}: {message}")

# Sistema de notificaciones depende de la abstracción
class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message, recipient):
        self.sender.send(message, recipient)

# Pruebas

email_service = NotificationService(EmailSender())
sms_service = NotificationService(SMSSender())
push_service = NotificationService(PushSender())
email_service.notify("Hola, este es un correo", "ana@mail.com")
sms_service.notify("Hola, este es un SMS", "+123456789")
push_service.notify("Hola, esta es una notificación PUSH", "UsuarioApp1")
