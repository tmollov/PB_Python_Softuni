hund = {
    "summer" : 0.3,
    "winter" : 0.7
}

tho = {
    "summer" : 0.4,
    "winter" : 0.8
}

budget = float(input())
season = input().lower()

country = ""
result = 0.0
if budget <= 100:
    result = budget * hund[season]
    country = "Bulgaria"
elif budget > 100 and budget <= 1000:
    result = budget * tho[season]
    country = "Balkans"
else :
    result = budget * 0.9
    country = "Europe"

print(f"Somewhere in {country}")
if season == "summer" and country in ["Bulgaria","Balkans"]:
    print(f"Camp - {result:.2f}")
else :
    print(f"Hotel - {result:.2f}")

