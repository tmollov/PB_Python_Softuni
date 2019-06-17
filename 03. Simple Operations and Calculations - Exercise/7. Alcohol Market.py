whiskeyCost = float(input())

rakiaPrice = whiskeyCost /2 
winePrice = rakiaPrice - (0.4 * rakiaPrice)
beerPrice = rakiaPrice - (0.8 * rakiaPrice)

beers = float(input())  * beerPrice
wines = float(input()) * winePrice
rakia = float(input()) * rakiaPrice
whiskeys = float(input()) * whiskeyCost 

alcoholPrice = (beers + wines + rakia+ whiskeys)

print('%.2f' % round((beers + wines + rakia+ whiskeys),2))