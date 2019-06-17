quota = int(input())

day = 1
fishCount = 0
profit = 0
lost = 0
while True:
    if quota < day:
        print("Lyubo fulfilled the quota!")
        break
    fish = input()
    if fish == "Stop":
        break
    kg = float(input())
    fishPrice = 0
    for ch  in fish:
        a = ord(ch)
        fishPrice += a
    fishPrice = fishPrice / kg

    if day % 3 == 0:
        profit += fishPrice
    else:
        lost += fishPrice
    day+=1
    fishCount += 1

if profit >= lost:
    print(f"Lyubo's profit from {fishCount} fishes is {(profit-lost):.2f} leva.")
else:
    print(f"Lyubo lost {(lost-profit):.2f} leva today.")