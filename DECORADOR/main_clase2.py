'''Decorador de Clase en Python'''

'''Un decorador de clase es una función que toma una clase como argumento y devuelve una clase modificada. A continuación, 
se presenta un ejemplo básico de un decorador de clase:'''


def mi_decorador_de_clase(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def nueva_funcion(self):
            print("Esta es una nueva función agregada por el decorador")

    return Wrapper

@mi_decorador_de_clase
class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

obj = MiClase("Juan")
obj.saludar()  # Hola, mi nombre es Juan
obj.nueva_funcion()  # Esta es una nueva función agregada por el decorador
'''

Explicación Paso a Paso

1. Definir el Decorador: Se define una función mi_decorador_de_clase que toma una clase cls como argumento.
2. Crear una Clase Wrapper: Dentro del decorador, se crea una clase Wrapper que envuelve la clase original.
3. Inicializar la Clase Wrapper: En el método __init__ de la clase Wrapper, se crea una instancia de la clase original y se asigna a self.wrapped.
4. Redireccionar Atributos: Se define el método __getattr__ para redireccionar los atributos y métodos de la clase original a la instancia self.wrapped.
5. Agregar Nueva Funcionalidad: Se define una nueva función nueva_funcion dentro de la clase Wrapper que no existe en la clase original.
6. Devolver la Clase Wrapper: El decorador devuelve la clase Wrapper modificada.
7. Aplicar el Decorador: Se aplica el decorador @mi_decorador_de_clase a la clase MiClase.
8. Crear una Instancia: Se crea una instancia de la clase MiClase decorada.
9. Acceder a Atributos y Métodos: Se accede a los atributos y métodos de la clase original y a la nueva función agregada por el decorador.

Ventajas de los Decoradores de Clase

- Modificación de Comportamiento: Los decoradores de clase permiten modificar el comportamiento de una clase sin alterar su código original.
- Reutilización de Código: Los decoradores de clase pueden ser reutilizados en diferentes clases para agregar funcionalidades comunes.
- Flexibilidad: Los decoradores de clase ofrecen una forma flexible de extender la funcionalidad de las clases sin afectar su estructura interna.

En resumen, los decoradores de clase son una herramienta poderosa en Python que permiten modificar y extender la funcionalidad de las clases de manera elegante y flexible.
'''