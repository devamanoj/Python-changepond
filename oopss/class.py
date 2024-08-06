class Student:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def display(self):
        print(f'{self.firstname} {self.lastname}')
obj1=Student('devanathan','.a')
obj1.display()