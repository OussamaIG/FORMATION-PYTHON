import random
array = []

for i in range(21):
    array.append(random.randint(1,45365))


print(array)
print(array[:5])
print(array[-5:])
print(array[::3])
print(array[::-1])