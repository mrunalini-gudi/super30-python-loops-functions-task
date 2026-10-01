#Menu-Driven Calculator
while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 6:
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if choice == 1:
        result = num1 + num2
        print("Result:", result)
    elif choice == 2:
        result = num1 - num2
        print("Result:", result)
    elif choice == 3:
        result = num1 * num2
        print("Result:", result)
    elif choice == 4:
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Division by zero is not allowed.")
    elif choice == 5:
        if num2 != 0:
            result = num1 % num2
            print("Result:", result)
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid choice.")