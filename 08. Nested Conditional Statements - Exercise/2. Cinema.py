projection = input().lower()

price = float(input()) * float(input())

if projection == "premiere":
    price *= 12.0
elif projection == "normal":
    price *= 7.50
else :
    price *= 5.0

print(f"{price:.2f}")