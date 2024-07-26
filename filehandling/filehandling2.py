import os

def create_file(filename):
    if os.path.exists(filename):
        print('File already exists.')
    else:
        file_create = open(filename, 'w')
        #file_create.close()

def copy_content(source, destination):
    if os.path.exists(source):
        src_file = open(source, 'r')
        content = src_file.read()
       # src_file.close()

        dest_file = open(destination, 'w')
        dest_file.write(content)
       # dest_file.close()

        print(f'Content copied from {source} to {destination}')
    else:
        print(f'Source file {source} does not exist.')

def main():
    print('Enter the name of the source file:')
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
