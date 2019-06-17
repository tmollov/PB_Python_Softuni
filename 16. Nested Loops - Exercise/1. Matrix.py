a = int(input())
b = int(input())
c = int(input())
d = int(input())

for ff in range(a,b+1):
    for fs in range(a,b+1):
        for sf in range(c,d+1):
            for ss in range(c,d+1):
                if ff+ss == fs+sf and (ff != fs) and (sf != ss):
                    print(f"{ff}{fs}")
                    print(f"{sf}{ss}\n")