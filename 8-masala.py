import os
os.system("cls")

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Bike(Vehicle):
    def __init__(self, brand, speed, type):
        super().__init__(brand, speed)
        self.type = type

bike1 = Bike("Giant", 25, "mountain")
bike2 = Bike("Trek", 30, "road")
bike3 = Bike("Specialized", 28, "mountain")

bikes = [bike1, bike2, bike3]

for b in bikes:
    print("Brand:", b.brand, "| Speed:", b.speed, "| Type:", b.type)
