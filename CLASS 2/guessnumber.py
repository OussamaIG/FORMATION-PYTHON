import random

secret = random.randint(1, 10)

guess = int(input("Guess a number between 1 and 10: "))

if guess < secret:
    print("Too low!")
elif guess > secret:
    print("Too high!")
else:
    print("Congratulations! You guessed it right!")