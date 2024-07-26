course = ['', 'python', 'java', ',,', 'angular']

# Use filter to apply a lambda function to each item in the list
filtered_course = list(filter(lambda s: isinstance(s, str) and s != '', course))

# Using a for loop to print each item in the filtered list
for item in filtered_course:
    print(item)

# Output list
print(filtered_course)  # Output: ['python', 'java', 'angular']
