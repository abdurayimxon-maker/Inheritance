import os
os.system("cls")

class Building:
    def __init__(self, adress): 
        self.adress = adress


class School(Building):
    def __init__(self, adress, student_count):
        super().__init__(adress)
        self.student_count = student_count

school1 = School("Toshkent  Olmazor ko'chasi 12", 500)

print("Manzil:", school1.adress)
print("O'quvchilar soni:", school1.student_count)