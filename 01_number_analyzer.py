#Number Analyzer using for loop
number = int(input("Enter a number: "))
even_count = 0
odd_count = 0
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, "is Even")
        even_count += 1
    else:
        print(i, "is Odd")
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
