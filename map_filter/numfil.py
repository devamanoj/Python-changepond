product_id = ['HEM-234', 'HEM-123', 'HEM-566']
 
def remove_chr(val):
    num = ""
    for i in val:
        if i>="0" and i<="9":
            num += i
    return int(num)
 
filtered_id = list(map(remove_chr, product_id))
print(filtered_id)