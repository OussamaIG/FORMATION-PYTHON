import random

temp = random.randint(-10, 40)

print(temp)

if temp > 0:
    if temp < 30:
        print("It's a warm day.")
    else :
        print("It's a hot day.")
else:
    print("It's a cold day.")