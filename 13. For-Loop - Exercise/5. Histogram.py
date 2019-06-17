count = int(input())
p = [0,0,0,0,0]

for i in range(count):
    num = int(input())
    if num < 200:
        p[0] += 1
    elif num >= 200 and num < 400:
        p[1] += 1
    elif num >= 400 and num < 600:
        p[2] += 1
    elif num >= 600 and num < 800:
        p[3] += 1
    elif num >= 800:
        p[4] += 1

print(f"{(p[0]/count)*100:.2f}%")
print(f"{(p[1]/count)*100:.2f}%")
print(f"{(p[2]/count)*100:.2f}%")
print(f"{(p[3]/count)*100:.2f}%")
print(f"{(p[4]/count)*100:.2f}%")