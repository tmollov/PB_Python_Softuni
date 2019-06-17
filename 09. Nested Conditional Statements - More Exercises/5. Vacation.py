camp = {"summer": 0.65, "winter": 0.45}
hut = {"summer": 0.8, "winter": 0.6}
hotel = {"summer": 0.9, "winter": 0.9}
location = {"summer": "Alaska", "winter":"Morocco"}
budget = float(input())
season = input().lower()

if budget <= 1000:
    print(f'{location[season]} - Camp - {(budget * camp[season]):.2f}')
elif budget > 1000 and budget <= 3000:
    print(f'{location[season]} - Hut - {(budget * hut[season]):.2f}')
elif budget > 3000:
    print(f'{location[season]} - Hotel - {(budget * hotel[season]):.2f}')