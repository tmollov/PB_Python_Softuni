campaignDayCount = int(input())
confectioner = int(input())
cakeCount = int(input()) * 45
waffleCount = int(input()) * 5.8
pancakeCount = int(input()) * 3.2

moneyForDay = (cakeCount + waffleCount + pancakeCount) * confectioner
moneyGained = moneyForDay * campaignDayCount
moneyAfterCampaignCost = moneyGained - (moneyGained/8)
print('%.2f' % round(moneyAfterCampaignCost,2 ))