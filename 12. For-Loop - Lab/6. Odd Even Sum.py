import math

count = int(input())

firstSum = 0
secondSum = 0

for i in range(count):
    if i % 2 == 0:
        firstSum += int(input())
    else:
        secondSum += int(input())



if firstSum == secondSum:
    print(f"Yes\nSum = {firstSum}")
else:
    print(f"No\nDiff = {int(math.fabs(firstSum - secondSum))}")