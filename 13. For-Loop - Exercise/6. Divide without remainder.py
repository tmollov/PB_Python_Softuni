count = int(input())
p = [0,0,0]

for i in range(count):
    num = int(input())
    if num % 2 == 0:
        p[0] += 1
    if num % 3 == 0:
        p[1] += 1
    if num % 4 == 0:
        p[2] += 1

print(f"{(p[0]/count)*100:.2f}%")
print(f"{(p[1]/count)*100:.2f}%")
print(f"{(p[2]/count)*100:.2f}%")