import math
sushiZone = {
    'sashimi' : 4.99,
    'maki' : 5.29,
    'uramaki' : 5.99,
    'temaki' : 4.29
}
sushiTime = {
    'sashimi' : 5.49,
    'maki' : 4.69,
    'uramaki' : 4.49,
    'temaki' : 5.19
}
sushiBar = {
    'sashimi' : 5.25,
    'maki' : 5.55,
    'uramaki' : 6.25,
    'temaki' : 4.75
}
asianPub = {
    'sashimi' : 4.50,
    'maki' : 4.80,
    'uramaki' : 5.50,
    'temaki' : 5.50
}

sushi = input().lower()
bar = input()
portions = int(input())
shipping = input().lower()

price = 0
if bar.lower() not in ["sushi zone","sushi time","sushi bar","asian pub"]:
    print(f"{bar} is invalid restaurant!")
    exit()
else :
    bar = bar.lower()
    if bar == "sushi zone":
        price = portions * sushiZone[sushi]
    elif bar == "sushi time":
        price = portions * sushiTime[sushi]
    elif bar == "sushi bar":
        price = portions * sushiBar[sushi]
    elif bar == "asian pub":
        price = portions * asianPub[sushi]

if shipping == "y":
    price += price * 0.2

print(f"Total price: {math.ceil(price)} lv.")