daysOfStay = float(input()) - 1
typeOfStay = input()
rating = input()

overnightPrice = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00,
}

daysMin = {
    "room for one person": 0,
    "apartment": 0.3,
    "president apartment": 0.1
}

daysMid = {
    "room for one person": 0,
    "apartment": 0.35,
    "president apartment": 0.15
}

daysMax = {
    "room for one person": 0,
    "apartment": 0.5,
    "president apartment": 0.2
}

finalPrice = overnightPrice[typeOfStay] * daysOfStay

if daysOfStay <= 10:
    finalPrice -= finalPrice * daysMin[typeOfStay]
elif daysOfStay > 10 and daysOfStay <= 15:
    finalPrice -= finalPrice * daysMid[typeOfStay]
elif daysOfStay > 15:
    finalPrice -= finalPrice * daysMax[typeOfStay]

if rating == "positive":
    finalPrice += finalPrice * 0.25
else:
    finalPrice -= finalPrice * 0.1

print("%.2f" % finalPrice)