#Bank Account Mini Application
history = []
balance = 0.0
def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    return balance + amount
def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds.")
        return 0
    else:
        return amount
def check_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")
def transaction_history(history):
    if history:
        print("Transaction History:")
        for transaction in history:
            print(transaction)
    else:
        print("No transactions yet.")
while True:
    print("\nWelcome to the Bank Account Mini Application!")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        balance = deposit(balance)
        history.append(f"Deposited: ${balance:.2f}")
    elif choice == '2':
        amount = withdraw(balance)
        if amount > 0:
            balance -= amount
            history.append(f"Withdrew: ${balance:.2f}")
    elif choice == '3':
        check_balance(balance)
    elif choice == '4':
        transaction_history(history)
    elif choice == '5':
        print("Thank you for using the Bank Account Mini Application!")
        break
    else:
        print("Invalid choice. Please try again.")
