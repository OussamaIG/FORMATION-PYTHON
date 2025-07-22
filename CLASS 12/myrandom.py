import random

#random number between 0-1
print(random.random())
#random number between s and e
print(random.randint(1,65465))

choices = ["orange", "apple", "bananna", "lemon"]
#pick a random choice from array
print(random.choice(choices))

#pick two random choices from the array
print(random.sample(choices, 2))

#change the order of the array
random.shuffle(choices)
print(choices)