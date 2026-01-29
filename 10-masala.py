import os
os.system("cls")


class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class Laptop(Product):
    def __init__(self, title, price, cpu_model):
        super().__init__(title, price)
        self.cpu_model = cpu_model

laptop1 = Laptop("Dell XPS", 1500, "Intel i7")
laptop2 = Laptop("MacBook Pro", 2500, "M1")
laptop3 = Laptop("HP Spectre", 1800, "Intel i5")

laptops = [laptop1, laptop2, laptop3]

eng_qimmat = max(laptops, key=lambda x: x.price)

print("Eng qimmat laptop:", eng_qimmat.title, "| Narxi:", eng_qimmat.price)