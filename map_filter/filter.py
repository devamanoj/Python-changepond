# check the number is greater and equal to 70 and less than and equal to 90
def chk(number):
    if 70 <= number <= 90:
        return number

def main():
    size = int(input('Enter the size: '))
    numbers = []
    print('Enter values:')
    for i in range(size):
        value = int(input())
        numbers.append(value)
    print('UserList:', numbers)

    filtered = list(filter(chk, numbers))
    print('Filtered list:', filtered)

if __name__ == "__main__":
    main()
