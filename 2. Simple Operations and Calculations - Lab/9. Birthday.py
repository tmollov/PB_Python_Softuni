length = int(input())
width = int(input())
heigth = int(input())
procent = 1 - (float(input()) * 0.01)

aquariumArea = (length * width * heigth) * 0.001
result = aquariumArea * procent
print("%.3f" % round(result,3))