#Multiplication Table Generator
number = int(input("Enter a number: "))
end = int(input("Enter the table endpoint: "))
for i in range(1, end + 1):
    print(f"{number} x {i} = {number * i}")
