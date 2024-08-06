class Circle:
    PI = 3.14
 
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Accept()
 
    def Accept(self):
        print('Enter the value')
        self.Radius = int(input())
cls1 = Circle()
