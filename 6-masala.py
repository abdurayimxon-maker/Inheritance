import os
os.system("cls")

class Food:
    def __init__(self, name):
        self.name = name

class Fruit(Food):
    def __init__(self, name, vitamin):
        super().__init__(name)
        self.vitamin = vitamin

fruit1 = Fruit("Olma", "C")

print("Nomi:", fruit1.name)
print("Vitamini:", fruit1.vitamin)
