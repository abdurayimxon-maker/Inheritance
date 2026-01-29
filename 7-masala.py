import os
os.system("cls")


class Worker:
    def __init__(self, full_name, salary):
        self.full_name = full_name
        self.salary = salary

class Programmer(Worker):
    def __init__(self, full_name, salary, language):
        super().__init__(full_name, salary)
        self.language = language

prog1 = Programmer("Ali", 2000, "Python")
prog2 = Programmer("Vali", 2500, "Java")
prog3 = Programmer("Gulshan", 2200, "C++")

programmers = [prog1, prog2, prog3]

for p in programmers:
    print("Ism:", p.full_name, "| Maosh:", p.salary, "| Til:", p.language)
