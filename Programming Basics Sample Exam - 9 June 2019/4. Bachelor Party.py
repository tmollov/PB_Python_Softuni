singerPrice = int(input())

income = 0
guests = 0
while True:
    n = input()
    if n == "The restaurant is full":
        break
    n = int(n)
    if n < 5:
        income += n * 100
    else :
        income += n * 70
    guests += n

income -= singerPrice

if income >= 0:
    print(f"You have {guests} guests and {income} leva left.")
else :
    print(f"You have {guests} guests and {income + singerPrice} leva income, but no singer.")