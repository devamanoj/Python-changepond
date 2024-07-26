from functools import reduce

def get_size():
    return int(input('Enter the size: '))

def get_numbers(size):
    numbers = []
    print('Enter values:')
    for _ in range(size):
        value = int(input())
        numbers.append(value)
    return numbers

def cube_numbers(numbers):
    return list(map(lambda num: num**3, numbers))

def sum_numbers(numbers):
    return reduce(lambda num1, num2: num1 + num2, numbers)

def main():
    size = get_size()
    numbers = get_numbers(size)
    print('UserList:', numbers)

    map_list = cube_numbers(numbers)
    print('map list:', map_list)
    print()

    reduce_value = sum_numbers(map_list)
    print('Reduce value:', reduce_value)

if __name__ == "__main__":
    main()
