x = float(input())
y = float(input())
h = float(input())

doorArea = 1.2 * 2
windowsArea = 2 * (1.5 * 1.5)
sideWalls = 2 * (x * y)
frontRearWalls = 2 * (x * x)
roofArea = (2 * (x * y)) + (2 * ((x * h) / 2))

greenArea = ((sideWalls + frontRearWalls) - (doorArea + windowsArea)) / 3.4
redArea = roofArea / 4.3
print('%.2f' % greenArea)
print('%.2f' % redArea)