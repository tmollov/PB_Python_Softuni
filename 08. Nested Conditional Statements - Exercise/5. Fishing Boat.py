
prices = {
    "spring" : 3000.0,
    "summer": 4200.0,
    "autumn" : 4200.0,
    "winter" : 2600.0
}

groupBudget = float(input())
season = input().lower()
fishersCount = int(input())

result = prices[season]

if fishersCount <= 6:
    result = result - (result * 0.1)
elif fishersCount > 7 and fishersCount <= 11 :
    result = result - (result * 0.15)
else :
    result = result - (result * 0.25)

if fishersCount % 2 == 0 and season != "autumn":
    result = result - (result * 0.05)

result = groupBudget - result

if result < 0:
    print(f"Not enough money! You need {result * -1.0:.2f} leva.")
else :
    print(f"Yes! You have {result:.2f} leva left.")