#syntax
class Student:
    #static method
    @staticmethod
    def RollNumber(y):
        print("inside static method:",y)
    #static method call
# Student.RollNumber(4435)
#using object
s1 = Student()
s1.RollNumber(101)