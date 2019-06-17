hallHeigth = (float(input()) * 100)
hallWidth = (float(input()) * 100 ) - 100

row = int(hallHeigth / 120)
col = int(hallWidth / 70)

print((row * col) - 3)