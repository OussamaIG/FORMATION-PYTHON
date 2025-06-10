#logical operators
# And operator both conditions must be true
age = int(input("Enter your age: "))
if age >= 0 and age <= 25:
    print("you were born in the 2000s")
# Or operator at least one condition must be true
elif age < 0 or age > 150:
    print("invalid age")
