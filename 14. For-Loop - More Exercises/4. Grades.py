studentsCount = int(input())

averageGrade = 0.0

poor = 0
good = 0
great = 0
top = 0

for i in range(studentsCount):
    num = float(input())
    if num >= 2.0 and num < 3.0:
        poor += 1
    if num >= 3.0 and num < 4.0:
        good += 1
    if num >= 4.0 and num < 5.0:
        great += 1
    if num >= 5:
        top += 1
    averageGrade += num

print(f"Top students: {((top/studentsCount)*100):.2f}%")
print(f"Between 4.00 and 4.99: {((great/studentsCount)*100):.2f}%")
print(f"Between 3.00 and 3.99: {((good/studentsCount)*100):.2f}%")
print(f"Fail: {((poor/studentsCount)*100):.2f}%")
print(f"Average: {(averageGrade / studentsCount):.2f}")