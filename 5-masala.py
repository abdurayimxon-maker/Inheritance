import os
os.system("cls")

class Device:
    def __init__(self, brend):
        self.brend = brend

class Phone(Device):
    def __init__(self, brend, ram):
        super().__init__(brend)
        self.ram = ram

phone1 = Phone("Samsung", "8GB")

print("Brend:", phone1.brend)
print("RAM:", phone1.ram)