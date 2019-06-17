while True:
    country = input()

    if country == "End":
        break
    
    budget = float(input())
    money = 0
    while budget > money:
        num = float(input())
        money += num
        num+=1
    print(f"Going to {country}!")