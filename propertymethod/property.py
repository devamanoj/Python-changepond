class Arithmatic:
    def __init__(self,value):
        self._value = value #protected attribute

    def getvalue(self):
        print('to retrive the value of \'_value\'')
        return self._value
    def setvalue(self,value):
        print('setting value to '+value)#new value/updated
        self._value = value
    def delvalue(self):
        print('Deleting the value')#deleting a value
        del self._value

    value = property(getvalue, setvalue, delvalue)
A1 = Arithmatic(12)
print(A1.value)

A1.value = 'Devanathan'
print(A1.value)