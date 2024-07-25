# import math

# # Example list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Calculate and print the square of each number in the list
# for i in numbers:
#     square = math.pow(i, 2)
#     print(f"The square of {i} is {square}")
# new_list = [i for i in range(1,11)]
# print('new_list:',new_list)

new_list = [i for i in range(1,11) if(i%2==0)]
print('new_list:',new_list)

# name = input("Enter a name: ")
# vowels = 'aeiouAEIOU'
# filtered_name = [char for char in name if char not in vowels]

# print('Filtered name:', filtered_name)
  # To ensure the cursor moves to the next line after printing the name

vowels = 'aeiouAEIOU'
name = 'Devanathan'
vowel1 = [i for i in name if i not in vowels]
print(vowel1)