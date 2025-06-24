import math

def PRIME(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0 :
            return False
    return True


if __name__ == "__main__":
    x = float(input("give a number :"))
    if (PRIME(x) == True):
        print(f"{x} is prime")
    else:
        print(f"{x} is not prime")