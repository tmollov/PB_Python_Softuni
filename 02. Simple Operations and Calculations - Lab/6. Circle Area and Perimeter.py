import math

r = float(input())
area = math.pi * r *r
perimeter = 2 * math.pi * r

print("%.2f" % round(area,2))
print("%.2f" % round(perimeter,2))