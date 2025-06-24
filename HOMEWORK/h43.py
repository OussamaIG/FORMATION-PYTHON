import h42, h41

n = int(input("Give a number : "))
fact_N = h42.FACT(n)

sum = 0
for i in range(1, fact_N+1):
    if h41.PRIME(i) == True:
        sum = sum + i

print(f"The sum of the Prime numbers from 1 to fact({n}) is : {sum}")