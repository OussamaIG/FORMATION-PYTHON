name = "Oussama"

#Functions
print(name.lower()) #lowercase
print(name.upper()) #uppercase
print(name.strip()) #remove whitespace from start and end

message = "Hello,my,name,is,Oussama"
print(message)

#Remove "," from the String and put the results in an array
message = message.split(",")
print(message)

#List to String
message = " ".join(message)
print(message)