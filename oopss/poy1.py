#example
class transport:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def display(self):
        print(f"{self.brand} and {self.model}")
class car(transport):
    pass

class boat(transport):
    pass

obj=car('hyundai',2007)
obj.display()
obj=boat('kappal',1999)
obj.display()