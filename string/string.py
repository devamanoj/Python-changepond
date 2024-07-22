# string formatting
# f-string
student_name =input('Enter your name:')
student_id =int(input('Enter your id number:'))
# print(f'Student Name {student_name.title()} \nStudent id: {student_id}')-title case
# print(f'Student Name {student_name.upper()} \nStudent id: {student_id}')-uppercase
# strinf -old format introduced in python 3.6 before earlier there was . format
print('Student Name {} \nStudent id: {}'.format(student_name,student_id))