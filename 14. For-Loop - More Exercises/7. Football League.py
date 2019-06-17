stadionCapacity = int(input())

fans = int(input())

a = 0
b = 0
v = 0
g = 0

for i in range(fans):
    fan = input().lower()
    if fan == "a":
        a += 1
    elif fan == "b":
        b += 1
    elif fan == "v":
        v += 1
    elif fan == "g":
        g += 1

print(f"{((a / fans)*100):.2f}%")
print(f"{((b / fans)*100):.2f}%")
print(f"{((v / fans)*100):.2f}%")
print(f"{((g / fans)*100):.2f}%")
print(f"{((fans / stadionCapacity)*100):.2f}%")