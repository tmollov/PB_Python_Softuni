daysOfWeek = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
fruits = ["banana","apple","orange","grapefruit","kiwi","pineapple","grapes"]

weekPrice = {
    "banana": 2.5,
    "apple": 1.2,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.7,
    "pineapple": 5.5,
    "grapes": 3.85,
}

weekendPrice = {
    "banana": 2.7,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.0,
    "pineapple": 5.6,
    "grapes": 4.2,
}

fruit = input().lower()
day = input().lower()
fruitCount = float(input())

price = 0

if fruit in fruits and day in daysOfWeek:
    if day == daysOfWeek[5] or day == daysOfWeek[6]:
        price = weekendPrice.get(fruit) * fruitCount
    else:
        price = weekPrice.get(fruit) * fruitCount

    print("%.2f" % price)
else:
    print("error")