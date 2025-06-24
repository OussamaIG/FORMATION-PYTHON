import helper1

while True:  
    try:
        b = 1
        a = int(input("Give the first number : "))
        helper1.Menu()
        operation = input("Operation : ")
        if(operation != "√" and operation != "!"):  
            b = int(input("Give the second number : "))
        result = helper1.calculer(a,operation,b)
        print(result)
        print("Exit.\nContinue.")
        choix = input("")
        if(choix.lower() == "exit"):
            break
    except Exception as e:
        print(e)