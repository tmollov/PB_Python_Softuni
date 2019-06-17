target = int(input())
combinations = 0
for a in range(target+1):
    for b in range(target+1):
        for c in range(target+1):
            for d in range(target+1):
                for e in range(target+1):
                    if a+b+c+d+e == target:
                        combinations += 1
print(combinations)