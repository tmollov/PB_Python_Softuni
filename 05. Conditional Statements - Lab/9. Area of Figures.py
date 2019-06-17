import math

form = input()

if form == "square":
    a = float(input())
    print('%.3f' % round(a*a, 3))
elif form == "rectangle":
    a = float(input())
    b = float(input())
    print('%.3f' % round((a * b), 3))
elif form == "circle":
    r = float(input())
    print('%.3f' % round((math.pi * (r * r)), 3))
else :
    a = float(input())
    h = float(input())
    print('%.3f' % round(((a*h)/2),3))
