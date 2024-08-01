try:
    num1 = int(input("enter an number1:"))
    num2 = int(input("enter an number2:"))
    result = num1/num2
    print(result)
    except ZeroDivisionError:
        print("ERROR: DENOMINATOR CANNOT BE ZERO")
    except ValueError:
        print("ERROR: ONLY NUMBERS ARE ALLOWED")