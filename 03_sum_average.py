#Sum and Average Without sum()
numbers = [10,20,30,40,50]
total = 0
for number in numbers:
    total += number
average = total / len(numbers)
print("Sum of numbers in list:", total)
print("Average of numbers in list:", average)
