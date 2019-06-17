budgetForActor = float(input())

while True:
    actorName = input()
    if actorName == "ACTION":
        break
    if actorName.__len__() > 15:
        budgetForActor -= budgetForActor * 0.2
        continue
    actorPrice = float(input())
     
    if budgetForActor < actorPrice:
        print(f"We need {(actorPrice - budgetForActor):.2f} leva for our actors.")
        exit()

    budgetForActor -= actorPrice
    
print(f"We are left with {budgetForActor:.2f} leva.")