lilyYears = int(input())
washmachinePrice = float(input())
toyPrice = float(input())

toysCount = 0
moneySave = 0
currentBirthdayBonus = 0
birthdayMoney = 10
brotherEarning = 0

for year in range(1,lilyYears+1):
    if year % 2 != 0:
        toysCount += 1
    else :
        moneySave += currentBirthdayBonus + birthdayMoney
        currentBirthdayBonus += birthdayMoney
        brotherEarning += 1

toyPrice *= toysCount

result = toyPrice + moneySave - brotherEarning

if result >= washmachinePrice:
    print(f"Yes! {result - washmachinePrice:.2f}")
else :
    print(f"No! {((result - washmachinePrice) * -1):.2f}")