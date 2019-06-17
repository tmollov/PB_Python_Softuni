import math

hallLength = float(input())
hallWidth = float(input())
wardrobeSide = float(input()) * 100

hallSize = (hallLength * 100) * (hallWidth * 100)
wardrobeSize = wardrobeSide**2
benchSize = hallSize / 10
freeSpace = hallSize - wardrobeSize - benchSize

dancerCount = freeSpace / 7040 
print('%.0f' % math.floor(dancerCount))