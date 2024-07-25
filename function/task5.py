def special_characters(string):
    special_characters = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/\\"
    
    for char in string:
        if char in special_characters:
            return True
    return False

def main():
    strings = input("Enter a string to check for special characters: ")

    if special_characters(strings):
        print("The string contains special characters.")
    else:
        print("The string does not contain any special characters.")

if __name__ == "__main__":
    main()
