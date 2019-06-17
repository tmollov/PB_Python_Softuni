winter = {
    "Dubai" : 45000,
    "Sofia" : 17000,
    "London" : 24000
}

summer = {
    "Dubai" : 40000,
    "Sofia" : 12500,
    "London" : 20250
}

movieBudget = float(input())
destination = input()
season = input().lower()
days = int(input())

result = 0
if season == "winter":
    result += winter[destination] * days
elif season == "summer" :
     result += summer[destination] * days

if destination == "Dubai":
    result -= result * 0.3
elif destination == "Sofia":
    result += result * 0.25

if movieBudget >= result:
    print(f"The budget for the movie is enough! We have {(movieBudget - result):.2f} leva left!")
else :
    print(f"The director needs {(result - movieBudget):.2f} leva more!")