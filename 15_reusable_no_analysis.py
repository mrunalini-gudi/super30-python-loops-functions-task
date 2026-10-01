#Reusable Number Analysis Function
def analyze_numbers(number: int) -> str:
    """checks if a number is positive, negative, or zero, even or odd, and prime or not prime."""
    if number < 0:
        result = f"{number} is a negative number."
    elif number > 0:
        result = f"{number} is a positive number."
    else:
        result = f"{number} is zero."

    if number % 2 == 0:
        result += f" {number} is an even number."
    else:
        result += f" {number} is an odd number."

    if number > 1:  
        for i in range(2, number):
            if number % i == 0:
                result += f" {number} is not a prime number."
                break
        else:
            result += f" {number} is a prime number."
    return result

print(analyze_numbers(6))
