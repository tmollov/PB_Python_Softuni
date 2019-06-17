import math

w = float(input())
l = float(input())
h = float(input())
ah = float(input())

rocketV = w * l * h
roomV = (ah + 0.4) * 2 * 2

result = math.floor(rocketV / roomV)

if result > 10:
    print("The spacecraft is too big. ")
elif result >= 3 and result <= 10 :
    print(f"The spacecraft holds {result} astronauts. ")
else :
    print("The spacecraft is too small.")