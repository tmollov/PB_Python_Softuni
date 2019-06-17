points = int(input())
bonusPoints = 0

if points <= 100:
    bonusPoints += 5
elif points > 100 and points < 1000 :
    bonusPoints += points * 0.2
elif points > 1000 :
    bonusPoints += points * 0.1

if points % 2 == 0:
    bonusPoints += 1

if  str(points)[-1] == "5": 
    bonusPoints += 2

print(bonusPoints)
print(points + bonusPoints)