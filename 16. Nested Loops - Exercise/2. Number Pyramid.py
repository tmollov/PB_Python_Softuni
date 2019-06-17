n = int(input())

numsToPrint = 1
currentNum = 1
while True:
    for i in range(numsToPrint):
        print(currentNum, end = " ")
        if currentNum == n:
            exit()
        currentNum+=1   
        
    numsToPrint+=1
    print()