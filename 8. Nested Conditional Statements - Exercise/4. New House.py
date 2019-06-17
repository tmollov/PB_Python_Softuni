floverPrice = {
    "roses" : 5.0,
    "dahlias" : 3.8,
    "tulips" : 2.8,
    "narcissus" : 3.0,
    "gladiolus" : 2.5
}

flover = input().lower()
floverQty = float(input())
budget = float(input())

price = floverPrice[flover] * floverQty

if flover == "roses" and floverQty > 80:
    price = price - (price* 0.1)
elif flover == "dahlias" and floverQty > 90:
    price = price - (price* 0.15)
elif flover == "tulips" and floverQty > 80:
    price = price - (price* 0.15)
elif flover == "narcissus" and floverQty < 120:
    price = price + (price* 0.15)
elif flover == "gladiolus" and floverQty < 80:
    price = price + (price* 0.2)

if price > budget:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
else :
    print(f"Hey, you have a great garden with {floverQty:.0f} {flover.title()} and {budget - price:.2f} leva left.")