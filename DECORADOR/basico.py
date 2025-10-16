def multiplica_por_dos(func):
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado * 2
    return wrapper

@multiplica_por_dos
def suma_numeros(a, b):
    return a + b

print(suma_numeros(3, 4))  # Salida: 14

def plus_one(number):
    def add_one(number):
        return number + 1


    result = add_one(number)
    return result
print(plus_one(4))


   