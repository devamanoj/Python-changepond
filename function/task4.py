def count_letter_frequency(string):
    frequency = {}
    for char in string:
        
        if ('a' <= char <= 'z') or ('A' <= char <= 'Z'): 
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
    return frequency

def main():
    string = input("Enter a string: ")
    frequency = count_letter_frequency(string)
    print("Letter frequency:")
    for letter in frequency:
        print(f"{letter}: {frequency[letter]}")

if __name__ == "__main__":
    main()
