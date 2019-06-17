moneyNeeded = float(input())
moneyAvail = float(input())

spendCounter = 0
days = 0

while True :
    operation = input()
    amount = float(input())

    if operation == "spend":
        spendCounter+=1
        if moneyAvail - amount < 0:
            moneyAvail = 0
        else:
            moneyAvail -= amount
    else :
        spendCounter = 0
        moneyAvail += amount
    
    days+=1
    if moneyAvail >= moneyNeeded:
        print(f"You saved the money for {days} days.")
        break

    if spendCounter >= 5:
        print("You can't save the money.")
        print(days)
        break
