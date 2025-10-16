'''
Asignar funciones a variables
Para empezar, creamos una función que sumará uno a un número cada vez que sea llamada. A continuación, asignaremos la función a una variable y utilizaremos esta variable para llamar a la función.
'''
def plus_one(number):
    return number + 1

add_one = plus_one
print(add_one(5))
'''
Definir funciones dentro de otras funciones 
A continuación, ilustraremos cómo puedes definir una función dentro de otra función en Python. Quédate conmigo, pronto descubriremos cómo todo esto es relevante para crear y comprender los decoradores en Python.
'''
def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
print(plus_one(4))

'''
Pasar funciones como argumentos a otras funciones
Las funciones también pueden pasarse como parámetros a otras funciones. Ilustrémoslo a continuación.'''


def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)


print(function_call(plus_one))

'''Funciones que devuelven otras funciones
Una función también puede generar otra función. Te lo mostraremos a continuación con un ejemplo.'''

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi
hello = hello_function()
print(hello())
'''Comprender los cierres
Python permite que una función anidada acceda al ámbito externo de la función que la encierra. Se trata de un concepto crítico en los decoradores, conocido como cierre.

Un cierre en Python es una función que recuerda el entorno en el que fue creada, incluso después de que ese entorno ya no esté activo. Esto significa que una función anidada puede "cerrar sobre" variables de su ámbito envolvente y seguir utilizándolas.

Los cierres son esenciales para entender los decoradores, porque éstos dependen de la capacidad de una función envolvente anidada para acceder y modificar el estado de la función decoradora que los encierra.

Ejemplo de cierre:'''
def outer_function(message):
    def inner_function():
        print(f"Message from closure: {message.upper()}")
    return inner_function

closure_function = outer_function("Hello, closures!")
print(closure_function())
'''Cuando creas un decorador, la función envolvente (dentro del decorador) es un cierre. 
Conserva el acceso a la función decorada y a cualquier estado o argumento adicional definido en la función decoradora. 
Por ejemplo:Aquí, wrapper es un cierre que recuerda la función greet y añade un comportamiento antes y después de su ejecución.'''

def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def greet():
    print("Hello!")
greet()
'''
Crear decoradores
Con estos requisitos previos fuera del camino, vamos a crear un sencillo decorador que convierta una frase a mayúsculas. Lo hacemos definiendo una envoltura dentro de una función adjunta. Como puedes ver es muy similar a la función dentro de otra función que hemos creado antes.
'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper
'''Nuestra función decoradora toma una función como argumento, por lo que definiremos una función y se la pasaremos a 
nuestro decorador. Antes aprendimos que podíamos asignar una función a una variable. Utilizaremos ese truco 
para llamar a nuestra función decoradora.'''

def say_hi():
    return 'hello there'

decorate = uppercase_decorator(say_hi)
print(decorate())

'''Sin embargo, Python nos proporciona una forma mucho más sencilla de aplicar decoradores. 
Simplemente utilizamos el símbolo @ delante de la función que queremos decorar. Vamos a demostrarlo en la práctica a continuación.
'''

@uppercase_decorator
def say_hi2():
    return 'hello there 2'

print(say_hi2())

'''Aplicar varios decoradores a una misma función
Podemos utilizar varios decoradores para una misma función. Sin embargo, los decoradores se aplicarán en el orden en que los hayamos 
llamado. A continuación definiremos otro decorador que divide la frase en una lista. 
A continuación, aplicaremos el decorador uppercase_decorator y split_string a una única función.'''
 
def split_string(function):
     
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper 

@split_string
@uppercase_decorator
def say_hi3():
    return 'hello there doble decorador'
print(say_hi3())
'''
Aceptar argumentos en funciones de decorador
A veces podemos necesitar definir un decorador que acepte argumentos. Lo conseguimos pasando los argumentos a la función envoltorio. 
Los argumentos se pasarán a la función que se esté decorando en el momento de la llamada.'''
def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1,arg2))
        function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))

cities("Madrid", "Toledo")
'''
Definición de decoradores de uso general
----------------------------------------
Para definir un decorador de propósito general que pueda aplicarse a cualquier función, 
utilizamos args y **kwargs. args y **kwargs recogen todos los argumentos posicionales y de palabra clave y los almacenan en 
las variables args y kwargs. args y kwargs nos permiten pasar tantos argumentos como queramos durante las llamadas a funciones.'''

def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args,**kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitrary_arguments

@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")

function_with_no_argument()
'''Veamos cómo utilizaríamos el decorador utilizando argumentos posicionales.'''
@a_decorator_passing_arbitrary_arguments
def function_with_arguments(a, b, c):
    print(a, b, c)

function_with_arguments(1,2,3)
'''Los argumentos de las palabras clave se pasan utilizando palabras clave. A continuación se muestra un ejemplo.'''

@a_decorator_passing_arbitrary_arguments
def function_with_keyword_arguments():
    print("This has shown keyword arguments")

function_with_keyword_arguments(first_name="Rufino", last_name="Prieto")

'''
Decoradores basados en clases
Aunque los decoradores basados en funciones son habituales, Python también te permite crear decoradores basados en clases, que proporcionan mayor flexibilidad y facilidad de mantenimiento, especialmente para casos de uso complejos. Un decorador basado en una clase es una clase con un método __call__ que le permite comportarse como una función.
'''
class UppercaseDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result.upper()

@UppercaseDecorator
def greet():
    return "hello there"

print(greet())
# Output: HELLO THERE
'''Cómo funciona:

El método __init__ inicializa el decorador con la función que se va a decorar.
El método __call__ se invoca cuando se llama a la función decorada, lo que permite al decorador modificar su comportamiento.
Ventajas de los decoradores basados en clases:

Decoradores con estado: Los decoradores basados en clases pueden mantener el estado mediante variables de instancia, a diferencia de los decoradores basados en funciones, que requieren cierres o variables globales.
Legibilidad: Para los decoradores complejos, encapsular la lógica en una clase puede hacer que el código esté más organizado y sea más fácil de entender.
Ejemplo de decorador con estado:
'''
class CallCounter:
    def __init__(self, function):
        self.function = function
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function {self.function.__name__} has been called {self.count} times.")
        return self.function(*args, **kwargs)

@CallCounter
def say_hello():
    print("Hello!")

say_hello()
say_hello()
# Output:
# Function say_hello has been called 1 times.
# Hello!
# Function say_hello has been called 2 times.
# Hello!

'''Otros usos comunes de los decoradores:

Registro: Rastrea las llamadas a funciones, los argumentos y los valores de retorno para depurar o auditar.

Autentificación: Aplica el control de acceso en aplicaciones web como Flask o Django.

Tiempo de ejecución: Mide y optimiza el tiempo de ejecución de las funciones para las tareas de rendimiento crítico.

Mecanismo de reintento: Reintenta automáticamente las llamadas a funciones fallidas, útil en operaciones de red.

Validación de la entrada: Valida los argumentos de la función antes de ejecutarla.

Resumen de los Decoradores de Python
Los decoradores modifican dinámicamente la funcionalidad de una función, método o clase sin tener que utilizar directamente subclases ni cambiar el código fuente de la función que se está decorando. Utilizar decoradores en Python también garantiza que tu código sea DRY(Don't Repeat Yourself). Los decoradores tienen varios casos de uso, como

Autorización en frameworks de Python como Flask y Django
Registro
Medir el tiempo de ejecución
Sincronización'''