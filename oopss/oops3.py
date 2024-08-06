class Demo:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
    def fun(self):
        print(f'{self.value1} {self.value2}')
    def gun(self):
        print(f'{self.value1} {self.value2}')
obj1 = Demo(22,33)
obj2 = Demo(44,55)
obj1.fun()
obj2.gun()