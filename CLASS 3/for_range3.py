start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
step = int(input("Enter the step value: "))

if start > end:
    print("Step must be negative or zero to count down.")
    while step >= 0:
        step = int(input("Please enter a negative step value: "))
elif start < end:
    print("Step must be positive to count up.")
    while step <= 0:
        step = int(input("Please enter a positive step value: "))
# This code will print "hello world" from start to end with a specific step using a for loop
for i in range(start, end, step):
    print(f"{i} - hello world")