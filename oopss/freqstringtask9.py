def count_string_in_file(file_name, search_string):
    with open(file_name, 'r') as file:
        content = file.read()
        frequency = content.count(search_string)
        return frequency

# Accept file name and string from the user
file_name = input("Enter the file name: ")
search_string = input("Enter the string to search for: ")

# Get the frequency of the string in the file
frequency = count_string_in_file(file_name, search_string)

print(f"The string '{search_string}' appears {frequency} times in the file '{file_name}'.")
