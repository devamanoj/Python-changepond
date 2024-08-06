class mobile:
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram
    def display(self):
        print(f'{self.brand} {self.ram}')
obj1 = mobile('motorola','4gb')
obj1.display()

