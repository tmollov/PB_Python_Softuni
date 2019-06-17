loops = int(input())
counter = 0
number = 0

minNumber = 2147483647

while counter < loops:
    number = int(input())
    if number < minNumber:
        minNumber = number
    counter +=1

print(minNumber)