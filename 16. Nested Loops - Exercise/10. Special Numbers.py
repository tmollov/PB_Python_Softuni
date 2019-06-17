num = int(input())

for i in range(1111,10000):
    a = int(i  % 10000 / 1000)
    b = int(i  % 1000 / 100)
    c = int(i  % 100 / 10)
    d = int(i  % 10)
    if a < 1 or b < 1 or c < 1 or d < 1:
        continue
    if (num / a == num // a) and (num / b == num // b) and (num / c == num // c) and (num / d == num // d):
        print(i,end = " ")