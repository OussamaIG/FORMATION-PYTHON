names = ["Jack", "Henry", "Hudlin", "Matheuss", "Alexia"]


#Direct Item Iteration ----- We cannot modify the values 
for name in names:
    print(name)


#Index Loop Iteration ----- We can modify the values
for i in range(len(names)):
    names[i] = names[i] + " " + "0" + str(i+1)

print(names)

#Enumerate Iteration
for i, name in enumerate(names):
    names[i] = names[i] + " " + "0" + str(i+1)

print(names)


#While
i = 0
while i < len(names):
    names[i] = names[i] + " " + "0" + str(i+1)
    i+=1

print(names)

#Printing using Slicing
for name in names[:3]:
    print(name)