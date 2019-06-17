winnerName = ""
winnerScore = 0
while True :
    name = input()
    if name == "STOP":
        break

    score = 0
    for ch in name:
        sm = ord(ch)
        score += sm
    
    if winnerScore < score:
        winnerName = name
        winnerScore = score
print(f"Winner is {winnerName} - {winnerScore}!")

# Solution with lists
#names = []
#namesSum = []
#while True :
#    name = input()
#    if name == "STOP":
#        break
#    names.append(name)
#
#for i in names:
#    nameSum = 0
#    for ch in i:
#        sm = ord(ch)
#        nameSum += sm
#    namesSum.append(nameSum)
#    
#winnerIndex = namesSum.index(max(namesSum))
#print(f"Winner is {names[winnerIndex]} - {namesSum[winnerIndex]}!")