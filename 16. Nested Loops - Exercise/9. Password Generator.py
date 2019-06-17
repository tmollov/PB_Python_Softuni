n = int(input())
l = int(input())

for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(97,97+l):
            for d in range(97,97+l):
                for e in range(1,n+1):
                    if a < e and b < e:
                        print(f"{a}{b}{chr(c)}{chr(d)}{e}", end=" ")