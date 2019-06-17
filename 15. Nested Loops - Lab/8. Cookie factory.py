count = int(input())

currentBatter = []
bakes = 0
while True: 
    if bakes == count:
        break
    el = input()
    if el == "Bake!" and ("flour" in currentBatter and "eggs" in currentBatter and "sugar" in currentBatter) :
        bakes+=1
        print(f"Baking batch number {bakes}...")
        currentBatter = []
        continue
    elif el == "Bake!":
        print("The batter should contain flour, eggs and sugar!")
    currentBatter.append(el)