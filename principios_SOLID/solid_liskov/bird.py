from abc import ABC, abstractmethod


# Incorrecto

class Bird:
    def fly(self):
        return "Flying"

class chicken(Bird):
    def fly(self):
        #return super().fly()  # This would violate Liskov Substitution Principle
        raise NotImplementedError("Chickens cannot fly")
    

# Correcto

class Bird:
    def move(self):
        return "Moving"

class chicken(Bird):
    def move(self):
        return "Walking"

bird = Bird()
print(bird.move())  # Output: Moving
chicken = chicken()
print(chicken.move())  # Output: Walking

bird = chicken()
print(bird.move())  # Output: Walking
chicken = Bird()
print(chicken.move())  # Output: Moving
