password = "cameljosha19"
numberoftries = 1

while True:
    user_ps = input("Enter the password: ")

    if user_ps == password:
        print("Access granted")
        break
    else:
        print("Incorrect password, try again")
    
    if numberoftries == 3:
        print("Too many attempts, access denied")
        break

    numberoftries += 1
# The code above is a simple password check program that allows the user to enter a password up to three times.      