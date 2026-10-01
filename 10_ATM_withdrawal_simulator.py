#ATM Withdrawal Simulator using while
balance = 10000
while True:
    print("Banking Options")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        amount = int(input("Enter the amount to deposit: "))
        balance += amount
        print("Amount deposited successfully.")
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")
    elif choice == 4:
        print("Thank you for using our banking services.")
        break
    else:
        print("Invalid choice. Please try again.")