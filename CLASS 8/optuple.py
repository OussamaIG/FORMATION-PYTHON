#declare a tuple
point = (42,12)

#print
print(point)

#length
print(len(point))

#check if value exists
if 2 in point:
    print("YES")
else:
    print("no")

#access
print(point[0])

#slicing same as in arrays

#iteration
for x in point:
    print(x)

#unpacking
a,b = point
print(a, b)

#tuple to list
lst = list(point)
print(lst)

#list to tuple
lst.append(3)
point = tuple(lst)
print(point)

