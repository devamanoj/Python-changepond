def sum_all(*args):
    count = 0
    for i in args:
        count += i
    return count 

output = sum_all(1,2,3,4,5)
print('addition ',output)