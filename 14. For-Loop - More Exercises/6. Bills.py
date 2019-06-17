months = int(input())

electricity = 0
water = months * 20
internet = months * 15
other = 0

for i in range(months):
    num = float(input())
    electricity += num
    num += 35
    other += num + (num * 0.2)

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {((electricity+water+internet+other)/months):.2f} lv")