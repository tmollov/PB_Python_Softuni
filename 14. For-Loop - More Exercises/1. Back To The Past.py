money = float(input())
yearToLive = int(input())

birthdays = 18
for i in range(1800, yearToLive+1):
    if i % 2 == 0:
        money -= 12000
    else:
        money -= 12000 + (birthdays * 50)
    birthdays += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else :
    print(f"He will need {(money * -1):.2f} dollars to survive.")