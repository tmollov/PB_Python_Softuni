product = input()
town = input().lower()
quantity = float(input())

products = ["coffee","water","beer","sweets", "peanuts"]

if town == 'sofia':
    if product == products[0]:
        print(quantity * 0.5)
    elif product == products[1]:
        print(quantity * 0.8)
    elif product == products[2]:
        print(quantity * 1.2)
    elif product == products[3] :
        print(quantity * 1.45)
    elif product == products[4]:
        print(quantity * 1.6)
elif town == 'plovdiv':
    if product == products[0]:
        print(quantity * 0.4)
    elif product == products[1]:
        print(quantity * 0.7)
    elif product == products[2]:
        print(quantity * 1.15)
    elif product == products[3] :
        print(quantity * 1.30)
    elif product == products[4]:
        print(quantity * 1.5)
elif town == 'varna':
    if product == products[0]:
        print(quantity * 0.45)
    elif product == products[1]:
        print(quantity * 0.7)
    elif product == products[2]:
        print(quantity * 1.1)
    elif product == products[3] :
        print(quantity * 1.35)
    elif product == products[4]:
        print(quantity * 1.55)