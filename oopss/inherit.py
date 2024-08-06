class Person:
    def __init__(self,identify,name):
        self.identify=identify
        self.name=name
    def Display(self):
        print(f"Name:{self.name} Id:{self.identify}")

class Employee(Person):
    def __init__(self,identify,name,salary):
        self.salary = salary
        #person.__init__(self,identify,name)
        super().__init__(identify,name)
    def Display(self):
        super().Display()
        print(f"Salary: {self.salary}")
# e1 = Person("Deva",123)
# e1.Display()
e1=Employee('Deva',123,15000)
e1.Display()