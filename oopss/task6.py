class Numbers:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def calculate(self):
        self.Value1 = int(input("Enter the first value: "))
        self.Value2 = int(input("Enter the second value: "))
    
    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value2 != 0:
            return self.Value1 / self.Value2
        else:
            return "Error! Division by zero"
    
# Create multiple objects and call instance methods
number1 = Numbers()
number2 = Numbers()


number1.calculate()
print("Addition:", number1.Addition())
print("Subtraction:", number1.Subtraction())
print("Multiplication:", number1.Multiplication())
print("Division:", number1.Division())


number2.calculate()
print("Addition:", number2.Addition())
print("Subtraction:", number2.Subtraction())
print("Multiplication:", number2.Multiplication())
print("Division:", number2.Division())
