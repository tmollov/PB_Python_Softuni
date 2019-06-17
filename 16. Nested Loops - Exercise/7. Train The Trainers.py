n = int(input())

score = 0
objects = 0
while True:
    currObj = input()
    if currObj == "Finish":
        break
    currScore = 0.0
    for j in range(n):
        currScore += float(input())
    score += currScore / n
    print(f"{currObj} - {(currScore / n):.2f}.")
    objects+=1
print(f"Student's final assessment is {(score / objects):.2f}.")