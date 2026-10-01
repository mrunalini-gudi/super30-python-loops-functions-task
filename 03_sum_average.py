#Sum and Average Without sum()
from functools import reduce
numbers = [10,20,30,40,50]
total = reduce(lambda x, y: x + y, numbers)
average = total / len(numbers)
print("Sum of numbers in list:", total)
print("Average of numbers in list:", average)
