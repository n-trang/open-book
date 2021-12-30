students = [("Alejandro", ["CompSci", "Physics"]),
            ("Justin", ["Math", "CompSci", "Stats"]),
            ("Ed", ["CompSci", "Accounting", "Economics"]),
            ("Margot", ["InfSys", "Accounting", "Economics", "CommLaw"]),
            ("Peter", ["Sociology", "Economics", "Law", "Stats", "Music"])]

for student in students:
    print(student[0], 'takes', len(student[1]), 'courses',)

students_take_cs = 0

for student in students:
    for subject in student[1]:
        if subject == "CompSci":
            students_take_cs += 1

print ('there are', students_take_cs, 'students take CS')