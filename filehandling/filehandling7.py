import os

def create_file(filename):
    if os.path.exists(filename):
        print('File already exists.')
    else:
        file_create = open(filename, 'w')
      

def copy_content(file1, file2):
    if os.path.exists(file1):
        src_file = open(file1, 'r')
        content = src_file.read()
      

        dest_file = open(file2, 'w')
        dest_file.write(content)
      

        print(f'Content copied from {file1} to {file2}')
    else:
        print(f' file {file1} does not exist.')

def main():
    print('Enter the name of the  file:')
    source_file = input()

    print('Enter the name of the destination file:')
    destination_file = input()

    create_file(destination_file)
    copy_content(source_file, destination_file)

if __name__ == "__main__":
    main()

# import os 
# def CreateFile(filename):
#     if(os.path.exists(filename)):
#         print('File is already exist')
#     else:
#         file_create = open(filename,'w')
    
# def main():
#     print('Enter the file name you want to create:')
#     file_name = input()

#     CreateFile(file_name)
# if __name__ == "__main__":
#     main()
#file handling
