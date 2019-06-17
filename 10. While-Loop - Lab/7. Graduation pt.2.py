studentName = input()
grade = 0
year = 1
IsPassed = True

while year <= 12 :
    currentGrade = float(input())
    if currentGrade >= 4.0:
        grade += currentGrade
    elif (IsPassed):
        IsPassed = False
    else :
        break
    year += 1
        
grade /= 12
if year >= 12:
    print(f"{studentName} graduated. Average grade: {grade:.2f}")
else :
    print(f"{studentName} has been excluded at {year-1} grade")