food = float(input())
souvenir = float(input())
hotel = float(input())

benzin = 54.39
result = benzin + (3 * food) + (3 * souvenir)
result += (hotel * 0.9) + (hotel * 0.85) + (hotel * 0.8)
print(f"Money needed: {result:.2f}")