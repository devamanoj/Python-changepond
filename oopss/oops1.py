# creating class and object
class student:
    graduation = 'B.Tech'
    def __init__(self,firstname,lastname):
        self.firstname = firstname #instance variables and properties
        self.lastname = lastname
    # def display(self): #instance method
    #     print(f'{self.firstname} {self.lastname}')
    
obj1 = student('devanathan','.a')
print(obj1.graduation)
# obj1.display()
