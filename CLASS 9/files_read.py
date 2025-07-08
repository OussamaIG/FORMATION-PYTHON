filename = "CLASS 9/data.txt"
mode = "r" 
contents = ""
#how to read the entire content of a file
with open(filename, mode) as f:
    contents = f.read()

# how to read line by line
with open(filename, mode) as f:
    line1 = f.readline()
    line2 = f.readline()

# how to read line by line all lines it returns a list
with open(filename, mode) as f:
    lines = f.readlines()

#iterate through the whole file
with open(filename, mode) as f:
    for line in f:
        print(line.strip())

#iterate word each 
contents = contents.split(" ")
for word in contents:
    print(word)