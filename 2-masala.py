class Transport:
    def __init__(self, model, year):
        self.model = model
        self.year = year

class Car(Transport):
    def __init__(self, model, year, color):
        super().__init__(model, year)
        self.color = color

car1 = Car("Toyota", 2020, "Qizil")

print("Model:", car1.model)
print("Yil:", car1.year)
print("Rang:", car1.color)