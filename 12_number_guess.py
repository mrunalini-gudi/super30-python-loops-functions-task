#Number Guessing Game
import random
number = random.randint(1, 100)
guess = int(input("Guess a number between 1 and 100: "))
count = 1
while guess != number:
    count += 1
    if guess < number:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Guess again: "))

print("Number of attempts to guess the correct number:", count)