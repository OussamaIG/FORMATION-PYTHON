from datetime import date

by = int(input("Enter the year you were born: "))
current_year = date.today().year
age = current_year - by
print(f"You are {age} years old.")