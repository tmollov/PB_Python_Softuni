import math

movieIncome = float(input())
statisCount = int(input())
wearPrice = float(input())

decor = movieIncome * 0.1
wearPrice *= statisCount

if statisCount > 150:
    wearPrice -= wearPrice * 0.1

result = movieIncome - (decor + wearPrice)

if result < 0:
    print("Not enough money!")
    print(f"Wingard needs {math.fabs(result):.2f} leva more.")
else :
    print("Action!")
    print(f"Wingard starts filming with {math.fabs(result):.2f} leva left.")
