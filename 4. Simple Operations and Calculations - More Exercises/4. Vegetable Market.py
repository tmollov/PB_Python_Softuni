import math

priceForVegetables = float(input())
priceForFruits = float(input())
kgVegetables = float(input())
kgFruits = float(input())

money = (priceForVegetables * kgVegetables + priceForFruits * kgFruits) / 1.94

if money - math.floor(money):
    print(f"{money:.15n}")
else :
    print(int(money))