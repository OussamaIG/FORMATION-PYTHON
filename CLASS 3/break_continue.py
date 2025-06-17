while True:
    n = int(input("Enter a number (or 0 to finish): "))
    if n > 0:
        # Negative numbers are not allowed, please try again.
        print("Negative numbers are not allowed, please try again.")
        continue
    if n == 0:
        break
    print(f"You entered: {n}")