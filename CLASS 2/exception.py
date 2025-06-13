try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))
    c = a / b
    print(f"The result of {a} divided by {b} is {c}.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

a = 10 + 5 
print(f"The sum of 10 and 5 is {a}.")

