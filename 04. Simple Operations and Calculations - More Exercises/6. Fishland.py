priceSkumriq = float(input())
priceCaca = float(input())
kgPalamud = float(input()) * (priceSkumriq + (priceSkumriq * 0.6))
kgSafrid = float(input()) * (priceCaca + (priceCaca * 0.8))
kgMidi = float(input()) * 7.5

print('%.2f' % round((kgPalamud + kgSafrid + kgMidi), 2))
