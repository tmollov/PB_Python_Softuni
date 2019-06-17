tableCount = int(input())
tableWidth = float(input())
tableHeigth = float(input())

rectangle = tableCount * (tableWidth + 2 * 0.30) * (tableHeigth + 2 * 0.30)
square = tableCount * (tableWidth / 2) * (tableWidth / 2)

priceInUSD = (rectangle * 7) + (square *9)
priceInBGN = priceInUSD * 1.85
print('%.2f USD' % round(priceInUSD,2))
print('%.2f BGN' % round(priceInBGN,2))