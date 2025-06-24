import math
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def div(a, b):
    try:
        return a/b
    except Exception as e:
        print(e)  

def FACT(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def mod(a, b):
    try:
        return a%b
    except Exception as e:
        print(e) 

def multi(a, b):
    return a*b

def power_nbr(a,b):
    s = 1
    for i in range(b):
        s = s * a
    return s


def calculer(a,choix, b):
    if choix == "+":
        r = add(a, b)
    elif choix == "-":
        r = sub(a, b)
    elif choix == "*":
        r = multi(a, b)
    elif choix == "/":
        r = div(a, b)
    elif choix == "%":
        r = mod(a, b)
    elif choix == "√":
        r = math.sqrt(a)
    elif choix == "^":
        r= pow(a, b)
    elif choix == "!":
        r = FACT(a)
    return r    

def Menu():
    print("[+][-][*][/][%][√][^][!]")