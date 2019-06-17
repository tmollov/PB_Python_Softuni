count = int(input())

firstNumber = int(input())
minNumber = firstNumber
maxNumber = firstNumber

for i in range(count-1):
    number = int(input())
    if number < minNumber:
        minNumber = number
    elif number > maxNumber:
        maxNumber = number 
    
print(f"Max number: {maxNumber}")
print(f"Min number: {minNumber}")