def calculate_sum(numbers):
   
    sum = 0
    for num in numbers:
        sum += num
    return sum
def find_maximum(numbers):
  
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:  
            max_num = num  
    return max_num
def main():
    

    size = int(input("Enter the size of the list: "))
    
    
    numbers = []
    
    
    for i in range(1, size + 1):
        number = int(input(f"Enter the number {i}: "))
        numbers.append(number)
    
   
    print("User List (numbers):", numbers)
    
    
    total_sum = calculate_sum(numbers)
    print("Sum of the list:", total_sum)

    max_num = find_maximum(numbers)
    print("Maximum number in the list:", max_num)

if __name__ == "__main__":
    main()
