#protected: these 

class Employee:
    def __init__(self,name,salary):
        self.name= name
        self._salary =salary  #protected attribute

    def DisplaySalaryInfo(self):
        print(f'{self.name} holding salary of {self._salary}')

e1 = Employee("manoj",25000)
print(e1.name)
print(e1._salary)
e1.DisplaySalaryInfo()