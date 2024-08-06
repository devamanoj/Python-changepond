# 2)Write a program which contains one class named as BookStore.
# Bookstore class contains two instance variables as Name , Author.
# That class contains one class variable as NoofBooks which is initialize to 0
# There is one instanace methods of class as Display which displays name, author and number of books.
# Initialise instance variable in init method by accepting the values from user as name and author.
# Inside init method increment value of NoOfBooks by one.
# After creating the class create the two objects of BookStore class as
# Obj1=Bookstore(“Linux System Programming”,”Robert Love”)
# Obj1.Display()  # Linux System Programming. No of books : 1

class BookStore:
    NoOfBooks = 0
    def __init__(self):
        self.Name = ""
        self.Author = ""
        BookStore.NoOfBooks+=1
    def create(self):
        self.Name = input('Enter the name:')
        self.Author = input('Enter the author:')
    def display(self):
        print(f'Name:{self.Name} \nauthor:{self.Author} \nnoOfbooks:{BookStore.NoOfBooks}')
obj1=BookStore()

obj1.create()
obj1.display()
obj2=BookStore()
obj2.create()
obj2.display()
#         def graduate_in(cls):
#         print('Graduation_in:',cls.graduation)
# student.Graduate = classmethod(student.graduate_in)
# student.Graduate()