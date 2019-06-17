gameTime = int(input())

score = 0
ten = 0
twenty = 0
thirty = 0 
fourty = 0
fifty = 0
invalid = 0

for i in range(gameTime):
    num = int(input())
    if num >= 0 and num < 10 :
        score += num * 0.2
        ten +=1
    elif num >= 10 and num < 20 :
        score += num * 0.3
        twenty += 1
    elif num >= 20 and num < 30 :
        score += num * 0.4
        thirty += 1
    elif num >= 30 and num < 40 :
        score += 50
        fourty += 1
    elif num >= 40 and num <= 50 :
        score += 100
        fifty +=1
    else :
        score -= score / 2
        invalid += 1

print(f"{score:.2f}")
print(f"From 0 to 9: {((ten/gameTime)*100):.2f}%")
print(f"From 10 to 19: {((twenty/gameTime)*100):.2f}%")
print(f"From 20 to 29: {((thirty/gameTime)*100):.2f}%")
print(f"From 30 to 39: {((fourty/gameTime)*100):.2f}%")
print(f"From 40 to 50: {((fifty/gameTime)*100):.2f}%")
print(f"Invalid numbers: {((invalid/gameTime)*100):.2f}%")