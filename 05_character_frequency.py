#Character Frequency Counter
string = input("Enter a string: ")
frequency =[]
for char in string:
    if char not in frequency:
        frequency.append(char)
        print(f"'{char}': {string.count(char)}")