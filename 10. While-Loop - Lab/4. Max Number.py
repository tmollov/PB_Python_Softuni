loops = int(input())
counter = 0
number = 0

maxNumber = -2147483648

while counter < loops:
    number = int(input())
    if number > maxNumber:
        maxNumber = number
    counter +=1

print(maxNumber)