hotSeasons = {1: 2.00, 2: 4.10, 3: 2.50}

coldSeasons = {1: 3.75, 2: 4.50, 3: 4.15}

hrizantemi = int(input())
rozi = int(input())
laleta = int(input())
season = input().lower()
IsHolyday = input().lower()

flowerCount = hrizantemi + rozi + laleta

price = 0
if season in ["spring", "summer"]:
    price = (hrizantemi *
             hotSeasons[1]) + (rozi * hotSeasons[2]) + (laleta * hotSeasons[3])
    if laleta > 7:
        price -= price * 0.05
else :
    price = (hrizantemi *
             coldSeasons[1]) + (rozi * coldSeasons[2]) + (laleta * coldSeasons[3])
    if rozi >= 10 and season == "winter":
        price -= price * 0.1

if IsHolyday == "y":
        price += price * 0.15

if flowerCount > 20:
        price -= price * 0.2   
price +=2

print(f'{price:.2f}')