import os
os.system("cls")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Manager(Employee):
    def __init__(self, name, position, team_size):
        super().__init__(name, position)
        self.team_size = team_size

manager1 = Manager("Sardor", "Project Manager", 10)

print("Ism:", manager1.name)
print("Pozitsiya:", manager1.position)
print("Jamoa hajmi:", manager1.team_size)
