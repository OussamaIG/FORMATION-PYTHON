age = int(input("Enter your age: "))
# est ce que l'age est moins que 15 : new gen
if age <= 15:
    print("NEW GEN")
# sinon si l'age est moins que 25 : gen z
elif age <= 25:
    print("GEN Z")
# Works in all other cases
else:
    print("MILENIAL")