try:
    items = ["bread","butter","jam","cheese"]
    num1 = int(input("enter an number1:"))
    #num2 = int(input("enter an number2:"))
    assert num1%2==0
except ZeroDivisionError:
    print("ERROR: DENOMINATOR CANNOT BE ZERO")
except ValueError:
    print("ERROR: ONLY NUMBERS ARE ALLOWED")
except IndexError:
    print("kindly use insert or append")
except AssertionError:
    print("Entered value is not matching the test condition")
else:
    print(num1,"is even")
finally:
    print("program is over")