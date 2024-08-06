class student:
    graduation = 'b.tech'
    def graduate_in(cls):
        print('Graduation_in:',cls.graduation)
student.Graduate = classmethod(student.graduate_in)
student.Graduate()
print()
class student:
    graduation = 'b.tech'
    @classmethod
    def graduate_in(cls):
        print('Graduation_in:',cls.graduation)
student.Graduate = classmethod(student.graduate_in)
student.graduate_in()

