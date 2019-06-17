word = input()

vowelSum = 0

for char in word:
    if char == 'a':
        vowelSum += 1
    if char == 'e':
        vowelSum += 2
    if char == 'i':
        vowelSum += 3
    if char == 'o':
        vowelSum += 4
    if char == 'u':
        vowelSum += 5

print(vowelSum)