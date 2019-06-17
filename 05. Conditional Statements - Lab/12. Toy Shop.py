import math

priceForTour = float(input())
puzzelCount = float(input())
dollCount = float(input())
bearCount = float(input())
minionCount = float(input())
truckCount = float(input())

totalPrice = (puzzelCount * 2.60) + (dollCount * 3.0) + (bearCount * 4.10) + (
    minionCount * 8.20) + (truckCount * 2.0)

toyCount = puzzelCount + dollCount + bearCount + minionCount + truckCount

if toyCount >= 50: 
    totalPrice = totalPrice - (totalPrice  * 0.25)
    totalPrice = totalPrice - (totalPrice * 0.1)
else :
    totalPrice = totalPrice - (totalPrice * 0.1)

if totalPrice >= priceForTour :
    print(f"Yes! {totalPrice - priceForTour:.2f} lv left.")
else :
    print(f"Not enough money! {math.fabs(totalPrice - priceForTour):.2f} lv needed.")
