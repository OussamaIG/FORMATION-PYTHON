def multipoint(x, y):
    x = x * 5
    y = y * 5
    point = (x,y)
    return point

a = multipoint(15,5)
x, y = a #unpack
print(x, y)