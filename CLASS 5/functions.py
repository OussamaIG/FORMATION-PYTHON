#functions
nums = [1,2,2,5]

#append(x) : Add an element at the end of the array
nums.append(12)
print(nums)

#pop() : Delete the last value of the array and return it
x = nums.pop()
print(nums)
print(x)

#pop(i): Delete and return the of value at index i
x = nums.pop(0)
print(nums)
print(x)

#insert(i, x): Puts x before position i
nums.insert(0, 3)
print(nums)

#remove(x): Delete the first occurrence of the value x:
nums.remove(2)
print(nums)

#len(obj): return the length
l = len(nums)
print(l) 