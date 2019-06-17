juniors = {
    "trail": 5.50,
    "cross-country": 8.00,
    "downhill": 12.25,
    "road": 20.00
}
seniors = {
    "trail": 7.00,
    "cross-country": 9.50,
    "downhill": 13.75,
    "road": 21.50
}

juniorCount = float(input())
seniorCount = float(input())
trace = input()
price = 0.0
if juniorCount + seniorCount >= 50 and trace == "cross-country":
    price = (juniorCount *
             (juniors[trace] -
              (juniors[trace] * 0.25))) + (seniorCount *
                                           (seniors[trace] -
                                            (seniors[trace] * 0.25)))
else:
    price = (juniorCount * juniors[trace]) + (seniorCount * seniors[trace])

price -= price * 0.05

print('%.2f' % round(price,2))