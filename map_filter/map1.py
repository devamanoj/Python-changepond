from functools import reduce
def main():
    size = int(input('Enter the size: '))
    numbers = []
    print('Enter values:')
    for i in range(size):
        value = int(input())
        numbers.append(value)
    print('UserList:', numbers)

    map_list = list(map(lambda num:num**3, numbers))
    print('map list:', map_list)
    print()
    reduce_list =reduce((lambda num1,num2:num1+num2),map_list)
    print('Reduce value:',reduce_list)
if __name__ == "__main__":
    main()