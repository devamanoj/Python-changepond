#def function_name():
# def add():
#     print('Inside additiion')
# add()


def add(value1):
    print('Inside additiion')
    print('Argument:',value1)
add(12)

def add(value1,value2):
    print('Inside additiion')
    print('Argument1:',value1)
    print('Argument2:',value2)
    Add = value1+value2
    return Add
Result =add(12,13)
print('addition of two numbers',Result)



    
# def Addition(value_01, value_02):
#     print('Inside Addition')
#     print('Argument 1:', value_01)
#     print('Argument 2:', value_02)
   
#     Add = value_01+value_02
#     Sub = value_01-value_02
   
#     print('Addition :',Add)
#     print('Subtraction :',Sub)
   
#     return Add, Sub
 
# Addition,Subtraction = Addition(12, 13)
 
# print('Addition Result:', AdditionResult)
# print('Subtraction Result:', SubtractionResult)
def greet():
    return "hello world!"
print(greet())