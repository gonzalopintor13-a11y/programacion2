import functools


class DecoratorExample:
    def __init__(self, value):
        self.value = value

    def value_printer(func):
        
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            print(f"Value: {self.value}")
            return result
        return wrapper

    def increment( func):
         
        def wrapper(self, *args, **kwargs):
            self.value += 1
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    def double( func):
         
        def wrapper(self, *args, **kwargs):
            self.value *= 2
            result = func(self, *args, **kwargs)
            return result
        return wrapper

    @value_printer
    @increment
    @double
    def opera(self):
        print("Operation performed.")

DecoratorExample(1).opera()
