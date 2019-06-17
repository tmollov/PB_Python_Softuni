low = {"spring": 0.75, "autumn": 0.75, "summer": 0.9, "winter": 1.05}
normal = {"spring": 0.95, "autumn": 0.95, "summer": 1.1, "winter": 1.25}
high = {"spring": 1.45, "autumn": 1.45, "summer": 1.45, "winter": 1.45}

season = input().lower()
kilometers = float(input())

if kilometers <= 5000:
    print(f'{(kilometers*low[season] * 4) * 0.9:.2f}')
elif kilometers > 5000 and kilometers <= 10000:
    print(f'{(kilometers*normal[season] * 4) * 0.9:.2f}')
elif kilometers > 10000 and kilometers <= 20000:
    print(f'{(kilometers*high[season] * 4) * 0.9:.2f}')