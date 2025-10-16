"""
SOLID - Principio de segregación de interfaces ISP

 Crea un gestor de impresoras.
 Requisitos:
 1. Algunas impresoras sólo imprimen en blanco y negro.
 2. Otras sólo a color.
 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 Instrucciones:
 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 2. Aplica el ISP a la implementación.
 3. Desarrolla un código que compruebe que se cumple el principio.
"""

from abc import ABC, abstractmethod

# Interface para imprimir
class IPrinter(ABC):
    @abstractmethod
    def print_document(self, content):
        pass

# Interface para escanear
class IScanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

# Interface para fax
class IFax(ABC):
    @abstractmethod
    def send_fax(self, number, content):
        pass



# Impresora blanco y negro
class ByWPrinter(IPrinter):
    def print_document(self, content):
        print(f"Imprimiendo en blanco y negro: {content}")

# Impresora a color
class ColorPrinter(IPrinter):
    def print_document(self, content):
        print(f"Imprimiendo en color: {content}")

# Impresora multifunción (print, scan, fax)
class MultiFunctionPrinter(IPrinter, IScanner, IFax):
    def print_document(self, content):
        print(f"Imprimiendo en multifunción: {content}")

    def scan_document(self):
        print("Escaneando documento...")

    def send_fax(self, number, content):
        print(f"Enviando fax al {number}: {content}")


#Pruebas
def test_printer(printer: IPrinter):
    printer.print_document("Mi documento de prueba")

def test_scanner(scanner: IScanner):
    scanner.scan_document()

def test_fax(fax: IFax):
    fax.send_fax("+123456789", "Documento para fax")

# Crear impresoras
bw = ByWPrinter()
color = ColorPrinter()
multi = MultiFunctionPrinter()

# Pruebas
print("Impresora B/W ")
test_printer(bw)

print("\nImpresora a color")
test_printer(color)

print("\nImpresora multifunción")
test_printer(multi)
test_scanner(multi)
test_fax(multi)
