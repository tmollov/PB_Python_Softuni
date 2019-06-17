targetNumber = int(input())

i = 10
if targetNumber < i:
    i = targetNumber + 1

for a in range(i):
    for b in range(i):
        for c in range(i):
            for d in range(i):
                for e in range(i):
                    for f in range(i):
                        if a*b*c*d*e*f == targetNumber:
                            print(f"{a}{b}{c}{d}{e}{f}", end = " ")
