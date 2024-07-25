def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
def main():
    operations = {
        '1': ('Addition', add),
        '2': ('Subtraction', subtract),
        '3': ('Multiplication', multiply),
        '4': ('Division', divide)
    }

    while True:
        print("Simple Calculator")
        # Directly print menu options from the dictionary
        for operation in operations.values():
            print(f"{list(operations.keys())[list(operations.values()).index(operation)]}) {operation[0]}")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice in operations:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"The result of {operation_name.lower()} is: {result}")
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
