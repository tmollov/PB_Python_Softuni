budget = float(input())
serials = int(input())

for i in range(0,serials):
    serialName = input()
    serialPrice = float(input())

    if serialName == "Thrones":
        serialPrice -= serialPrice * 0.5
    elif serialName == "Lucifer":
        serialPrice -= serialPrice * 0.4
    elif serialName == "Protector":
        serialPrice -= serialPrice * 0.3
    elif serialName == "TotalDrama":
        serialPrice -= serialPrice * 0.2
    elif serialName == "Area":
        serialPrice -= serialPrice * 0.1
    
    budget -= serialPrice

if budget >= 0 :
    print(f"You bought all the series and left with {budget:.2f} lv.")
else :
    print(f"You need {(budget * -1):.2f} lv. more to buy the series!")