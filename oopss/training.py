#Create a class Person with attributes name and age, and a method display() to print these attributes.
#class and object
class Person:
    def __init__(self,name,age): #constructor method and instance variables
        self.name = name
        self.age = age
    def display(self):
        print(f"name:{self.name} \nage:{self.age}")
# obj = Person('Devanathan',23)
# obj1 = Person('Rahul',22)
# obj.display()
# obj1.display()
# inheritance and Task: Create a class Student that inherits from Person and adds a new attribute student_id.
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def display(self):
        super().display()
        print(f"student id:{self.student_id}")
studen1 = Student("Devanathan",23,4435)
student2 = Student("Rahul",22,4446)
studen1.display()
student2.display()
