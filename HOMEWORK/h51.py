temps = []
max = None
min = None
sum = 0
while True:
    temp = input("Give a temperature (or q to quit): ")
    try :
        if max is None:
            max = int(temp)
        if min is None:
            min = int(temp) 
        if temp == "q":
            break
        else:
            if int(temp) > max:
                max = int(temp)
            elif int(temp) < min:
                min = int(temp)
            temps.append(int(temp))
            sum = sum + int(temp)
    except Exception as e:
        print(e)

print("\n")
print(temps)
print(f"Number of readings is : {len(temps)}\n")
print(f"Max Temp is {max}c | Min Temp is {min}c\n")
try:
    print(f"The average is {sum / len(temps):.1f}")
except Exception as e:
    print(e)
