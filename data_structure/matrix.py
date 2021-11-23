matrix = [
    [10,  20,  30,  40,  50],
    [60,  70,  80,  90, 100],
    [110,120, 130, 140, 150,00]
]
# matrix[row][column]

print(matrix[0][3])
print(matrix[1][-1])

grade = [
    ["joão", 3,6,7,9],
    ["Marai", 6,8,7,9],
    ["Carlos", 5,2,6,6],
    ["Marina", 10,7,6,3]
]

#   Repraved < rate >=60% approved

#rate = lambda grade: (grade[len(grade)-1]/(len(grade)) + rate(grade.pop())) if(len(grade) > 1) else 0 
def grades(student):
    if(len(student)> 1):
        n = student[-1]
        student.pop()
        return n + grades(student)
    else:
        return 0

for student in grade:
    row = list(student)
    if(grades(student) >= 40*0.6):
        print("%s approved" % student[0])
    else:
        print("%s reproved" % student[0])
