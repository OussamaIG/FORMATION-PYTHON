filename = "Class 9/students.csv"
mode = "r"

students = []

with open(filename, mode) as f:
    for line in f:
        students.append(line.strip().split(","))


student = students[0]
student[1] = "19"

with open(filename, "w") as f:
    for std in students:
        line = ",".join(std) + "\n"
        f.write(line)
