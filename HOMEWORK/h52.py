import random
array = []
even = []
def filter(a):
    if a % 2 == 0:
        return True
    else : 
        return False
    
for i in range(15):
    array.append(random.randint(1,54678))

print(array)

for x in array:
    if filter(x):
        array.remove(x)
        even.append(x)

print(array)
print(even)