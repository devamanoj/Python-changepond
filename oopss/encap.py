#public: these are accesible from outside the class

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def displaysalaryinfo(self):
        print(f'{self.name} holding salary of {self.salary}')
e1 = Employee('Ankita',25000)
print(e1.salary)
e1.displaysalaryinfo()