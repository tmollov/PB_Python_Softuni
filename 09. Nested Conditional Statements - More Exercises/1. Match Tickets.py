budget = float(input())
category = input()
peopleCount = int(input())

transportPrice = 0

if peopleCount in range(1,5):
    transportPrice = budget * 0.75
elif peopleCount in range(5,10):
    transportPrice = budget * 0.60
elif peopleCount in range(10,25):
    transportPrice = budget * 0.50
elif peopleCount in range(25,50):
    transportPrice = budget * 0.40
elif peopleCount >= 50:
    transportPrice = budget * 0.25

budget -= transportPrice
ticketPrice = 0
if category == "VIP":
    ticketPrice = 499.99 * peopleCount
else :
    ticketPrice = 249.99 * peopleCount 

result = budget - ticketPrice

if result >= 0:
    print(f'Yes! You have {result:.2f} leva left.')
else :
    result *= -1
    print(f'Not enough money! You need {result:.2f} leva.')