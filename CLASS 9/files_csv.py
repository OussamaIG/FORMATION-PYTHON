students = [
    ["Oussama", "24", "Data Analytics"], 
    ["Lotfi", "23", "Data Science"], 
    ["Abdou", "24", "Cyber Security"]
]

filename = "Class 9/students.csv"
mode = "a"

with open(filename, mode) as f:
    for std in students:
        line = ",".join(std) + "\n"
        f.write(line)
