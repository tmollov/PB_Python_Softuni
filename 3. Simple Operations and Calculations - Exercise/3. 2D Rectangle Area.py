x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

Xm = abs(x1 - x2)
Ym = abs(y1 - y2)

S = Xm * Ym
P = (Xm + Ym) * 2

print("%.2f" % S)
print("%.2f" % P)