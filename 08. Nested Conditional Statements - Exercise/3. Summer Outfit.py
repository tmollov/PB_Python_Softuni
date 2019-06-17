morning = {
    1: "Sweatshirt and Sneakers",
    2: "Shirt and Moccasins",
    3: "T-Shirt and Sandals"
}
afternoon = {
    1: "Shirt and Moccasins",
    2: "T-Shirt and Sandals",
    3: "Swim Suit and Barefoot"
}
evening = {
    1: "Shirt and Moccasins",
    2: "Shirt and Moccasins",
    3: "Shirt and Moccasins"
}

temp = int(input())
daytime = input().lower()

index = 0
if temp >= 10 and temp <= 18:
    index = 1
elif temp >= 18 and temp <= 24:
    index = 2
elif temp >= 25:
    index = 3

if daytime == "morning":
    print(f"It's {temp} degrees, get your {morning[index]}.")
elif daytime == "afternoon":
    print(f"It's {temp} degrees, get your {afternoon[index]}.")
elif daytime == "evening":
    print(f"It's {temp} degrees, get your {evening[index]}.")