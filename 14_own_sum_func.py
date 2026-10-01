#Create Your Own sum() Function
def my_sum(numbers: list) -> float:
    """Returns the sum of a list of numbers."""
    total = 0
    for i in numbers:
        total += i
    return total
print(my_sum([1, 2.8, 3, 4, 5.2]))