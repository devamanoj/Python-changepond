import os

def create_file(filename):
    if os.path.exists(filename):
        print('File already exists.')
    else:
        file_create = open(filename, 'w')
        file_create.close()

def copy_content(file1, file2):
    if os.path.exists(file1):
        src_file = open(file1, 'r')
        content = src_file.read()
        src_file.close()

        dest_file = open(file2, 'a')  # Append mode
        dest_file.write(content)
        dest_file.close()

        print(f'Content copied from {file1} to {file2}')
    else:
        print(f'File {file1} does not exist.')

def append_to_file(filename):
    if os.path.exists(filename):
        print('Enter the text you want to append:')
        user_text = input()

        dest_file = open(filename, 'a')  # Append mode
        dest_file.write(user_text + '\n')
        dest_file.close()

        print(f'Text appended to {filename}')
    else:
        print(f'File {filename} does not exist.')

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'File {filename} has been deleted.')
    else:
        print(f'File {filename} does not exist.')

def main():
    print('Enter the name of the source file:')
    source_file = input()

    print('Enter the name of the destination file:')
    destination_file = input()

    create_file(destination_file)
    copy_content(source_file, destination_file)

    print('Do you want to append text to the destination file? (yes/no)')
    answer = input().lower()

    if answer == 'yes':
        append_to_file(destination_file)

    print('Do you want to delete any file? (yes/no)')
    answer = input().lower()

    if answer == 'yes':
        print('Enter the name of the file to delete:')
        file_to_delete = input()
        delete_file(file_to_delete)

if __name__ == "__main__":
    main()
