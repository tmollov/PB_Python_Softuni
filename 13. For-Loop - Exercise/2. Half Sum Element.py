import math
count = int(input())
elements = []

for i in range(count):
    elements.append(int(input()))

maxElement = max(elements)
elements.pop(elements.index(maxElement))
result = sum(elements)

if maxElement == result:
    print(f"Yes\nSum = {result}")
else :
    print(f"No\nDiff = {int(math.fabs(maxElement - result))}")