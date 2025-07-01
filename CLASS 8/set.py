array = [64,12,2,2,5,78,78,12]

myset = set(array)
print(myset)

#add a value to the set
myset.add(45)
print(myset)
myset.add(4)
print(myset)
#remove a value \ raise error if missing
myset.remove(2)
print(myset)
# as as remove \ doesnt raise an error 
myset.discard(1546)
print(myset)
#pop the first element of the set
x = myset.pop()
print(x)
#clear all
myset.clear()
print(myset)

#check if set is empty
if myset == set():
    print("Empty")
