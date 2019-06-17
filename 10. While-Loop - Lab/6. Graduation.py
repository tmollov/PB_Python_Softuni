studentName = input()

grade = 0
counter = 1

while counter <= 12 :
    currentGrade = float(input())
    if currentGrade >= 4.0:
        grade += currentGrade
        counter += 1
grade /= 12
if grade >= 4.0:
    print(f"{studentName} graduated. Average grade: {grade:.2f}")