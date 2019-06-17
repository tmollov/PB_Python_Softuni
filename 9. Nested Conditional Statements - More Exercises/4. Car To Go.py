economy = {"summer": 0.35, "winter": 0.65}
compact = {"summer": 0.45, "winter": 0.80}
luxury = {"summer": 0.9, "winter": 0.9}
car = {"summer": "Cabrio", "winter":"Jeep"}
budget = float(input())
season = input().lower()

if budget <= 100:
    print("Economy class")
    print(f'{car[season]} - {(budget * economy[season]):.2f}')
elif budget > 100 and budget <= 500:
    print("Compact class")
    print(f'{car[season]} - {(budget * compact[season]):.2f}')
elif budget > 500:
    print("Luxury class")
    print(f'Jeep - {(budget * luxury[season]):.2f}')