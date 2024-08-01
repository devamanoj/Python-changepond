try:
    filename = input("Enter the filename: ")
    mode = input("Enter the file mode (r, w, a): ")
    
    with open(filename, mode) as file:
        if mode == 'r':
            content = file.read()
            print("File content:")
            print(content)
        elif mode == 'w':
            content = input("Enter the content to write: ")
            file.write(content)
            print("Content written to file.")
        elif mode == 'a':
            content = input("Enter the content to append: ")
            file.write(content)
            print("Content appended to file.")
        else:
            raise ValueError("Invalid mode. Use 'r', 'w', or 'a'.")

except FileNotFoundError:
    print("ERROR: File not found.")
except PermissionError:
    print("ERROR: Permission denied.")
except IsADirectoryError:
    print("ERROR: Expected a file but found a directory.")
except ValueError as ve:
    print(f"ERROR: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("File operation successful.")
finally:
    print("File handling program is over.")
