days = ["Error","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

day = int(input())

if day > 7 or day < 0:
    print(days[0])
else:
    print(days[day])