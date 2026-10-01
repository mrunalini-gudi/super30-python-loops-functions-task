#Find Maximum and Minimum Without max() / min()
numbers = [10, 20, 30, 40, 50]
max_number = numbers[0]
min_number = numbers[0]
for i in range(1, len(numbers)):
    if max_number < numbers[i]:
        max_number = numbers[i]
    if min_number > numbers[i]:
        min_number = numbers[i]
print("Maximum number:", max_number)
print("Minimum number:", min_number)

