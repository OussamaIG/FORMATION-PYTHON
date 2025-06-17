total = 0

while True:
    num = input("Enter a number (or 'q' to finish): ")
    if num.lower() == 'q':
        break
    total += int(num)

print(f"The total is: {total}")