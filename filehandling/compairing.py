import os
import filecmp

# Function to compare two files
def compare_files(file1, file2):
    if not os.path.exists(file1):
        print(f"{file1} does not exist")
    elif not os.path.exists(file2):
        print(f"{file2} does not exist")
    else:
        are_same = filecmp.cmp(file1, file2)
        if are_same:
            print(f"The files {file1} and {file2} are the same.")
            os.remove(file1)
            print(f"{file1} has been removed.")
        else:
            print(f"The files {file1} and {file2} are different.")

# Function to create a new file
def create_file(filename):
    if os.path.exists(filename):
        print('File already exists.')
    else:
        with open(filename, 'w') as file:
            pass  # Create an empty file
        print(f'{filename} has been created.')

# Function to copy content from one file to another
def copy_content(file1, file2):
    if os.path.exists(file1):
        with open(file1, 'r') as src_file:
            content = src_file.read()
        with open(file2, 'a') as dest_file:
            dest_file.write(content)
        print(f'Content copied from {file1} to {file2}')
    else:
        print(f'{file1} does not exist.')



# Function to delete a file
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'{filename} has been deleted.')
    else:
        print(f'{filename} does not exist.')

def main():
    print('Enter the name of the source file:')
    source_file = input()
    
    print('Enter the name of the destination file:')
    destination_file = input()

    create_file(destination_file)
    copy_content(source_file, destination_file)


    print('Do you want to compare files to check for duplicates? (yes/no)')
    if input().strip().lower() == 'yes':
        print('Enter the name of the second file to compare with the destination file:')
        file_to_compare = input()
        compare_files(destination_file, file_to_compare)

    print('Do you want to delete any file? (yes/no)')
    if input().strip().lower() == 'yes':
        print('Enter the name of the file to delete:')
        file_to_delete = input()
        delete_file(file_to_delete)

if __name__ == "__main__":
    main()
