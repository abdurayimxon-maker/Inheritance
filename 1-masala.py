import os
os.system("cls")

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.sound = "Woof"

    def make_sound(self):
       print("Woof...")

dog1 = Dog("Baron")

print("Itning nomi:", dog1.name)
dog1.make_sound()