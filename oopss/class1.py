class Myclass:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"hello {self.name} !")
obj = Myclass('devanathan')
obj.greet()