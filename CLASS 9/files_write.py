filename = "CLASS 9/names.txt"
filename2 = "CLASS 9/values.txt"
mode = "a"

#modes : w(to create an existing file) / a(create if missing, add to the end)
with open(filename, mode) as f:
    f.write("first line in the file\n")
    f.write("second line in the file\n")

#writing using a list
vals = ["1\n","15\n","23\n","56\n","89\n","2163\n"]
with open(filename2, mode) as f:
    f.writelines(vals)


