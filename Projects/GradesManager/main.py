import json
filename = "Projects/GradesManager/grades.csv"
mode = "r"

students = []

with open(filename, mode) as f:
    for line in f:
        students.append(line.strip().split(","))

for student in students:
    int_marks = list(map(lambda x : int(x), student[-3:]))
    avr = 0

    for mark in int_marks:
        avr = avr + mark
    if avr > 50 : sts = "PASS"
    else : sts = "FAIL"

    student.append(round(avr / len(int_marks),2))
    student.append(sts)

keys = ["name", "grade 1", "grade 2", "grade 3", "average", "status"]

students_dict = list(map(lambda student : dict(zip(keys, student)), students))

with open("Projects/GradesManager/finalgrades.json", "w") as f:
    json.dump(students_dict, f, indent=4)

    