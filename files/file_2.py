''' Add some extra functionality, a senior (8+) dog should say something else. '''

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark (self):
        if self.age < 8:
            print(f"{self.name} says: WOOF")
        else:
            print(f"{self.name} says: WOF")

brutus = Dog("Brutus", 4)
brutus.bark()

fifi = Dog("Fifi", 10)
fifi.bark()
