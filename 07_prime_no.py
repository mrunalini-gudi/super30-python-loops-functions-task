#Prime Number Finder
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for num in range(start, end + 1):
    if num > 1:
        count = 0
        for i in range(2, num):
            if num % i == 0:
                count = 1
                break
        if count == 0:
            print(num)
