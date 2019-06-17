firstNum = int(input())
secondNum = int(input())

if firstNum < secondNum : 
    firstNum, secondNum = secondNum, firstNum

print(firstNum)