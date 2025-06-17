start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Ensure that the starting number is less than the ending number
while start > end:
    print("Starting number must be less than ending number. Please try again.")
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

# This code will print "hello world" from start to end using a for loop
for i in range(start, end):
    print(f"{i} - hello world")