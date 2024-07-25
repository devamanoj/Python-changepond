def main():
    size = int(input('Enter the size: '))
    numbers = []
    print('Enter values:')
    for i in range(size):
        value = int(input())
        numbers.append(value)
    print('UserList:', numbers)

    filtered = list(filter(lambda x: 70 <= x <= 90, numbers))
    #filtered = list(filter(lambda values :values >= 70 and values <= 90,numbers))
    print('Filtered list:', filtered)

if __name__ == "__main__":
    main()


