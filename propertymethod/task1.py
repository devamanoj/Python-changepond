class Arithmatic:
    def __init__(self, value):
        self._value = value  # protected attribute

    @property
    def value(self):
        print('To retrieve the value of \'_value\'')
        return self._value

    @value.setter
    def value(self, value):
        print('Setting value to ' + str(value))  # updated value
        self._value = value

    @value.deleter
    def value(self):
        print('Deleting the value')  # deleting the value
        del self._value

# Example usage
A1 = Arithmatic(12)
print(A1.value)  # Retrieve the value

A1.value = 'Devanathan'  # Set a new value
print(A1.value)  # Retrieve the updated value

del A1.value  # Delete the value
