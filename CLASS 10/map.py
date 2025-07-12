import math
numbers = [1,2,35,64,64,64,3,2,9,1,3,16,43,3,16,456,0]

def multi(n):
    return n * 5

#how to use map (result = map(function, array))
new_nbrs = map(multi, numbers)

#using lambda
new_nbrs = map(lambda x: math.pow(x, 5), numbers)
print(list(new_nbrs))
