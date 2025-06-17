#Ask the user to make a choice
print("Welcome to the Calculator!")
print("Please choose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")

# Get the user's choice
choice = input("Enter the number of your choice (1-4): ")

try:
    # Get the two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    elif choice == '5':
        result = num1 % num2
        print(f"The result of {num1} % {num2} is: {result}")
    else:
        print("Invalid choice. Please run the program again and select a valid operation.")
except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed. Please enter a non-zero second number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Thank you for using the Calculator!")
# End of calculator1.py