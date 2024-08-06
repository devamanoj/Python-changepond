class Student:

    @staticmethod
    def RollNumber(y):
        print("Inside Static Method",y)

Student.RollNumber = staticmethod(Student.RollNumber)
Student.RollNumber(102)