# Function to calculate the power of a number
def power_nbr(a,b):
    s = 1
    for i in range(b):
        s = s * a
    return s
    
print(f"2 raised to the power of 3 is: {power_nbr(2, 3)}")

    