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
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            result += f" {number} is an prime number."
        else:
            result += f" {number} is an not a prime number."
    else:
        result += f" {number} is an not a prime number."
    return result

print(analyze_numbers(6))
