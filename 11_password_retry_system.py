#Password Retry System
password = input("Enter the password: ")
secret_password = "secret123"
count = 1
while password != secret_password and count < 3:
    print("Incorrect password. Try again.")
    password = input("Enter the password: ")
    count += 1

if password == secret_password:
    print("Access granted!")
else:
    print("Account Locked.")
