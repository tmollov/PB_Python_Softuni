import math
count = int(input())

pairs = []
maxdiff=0

if count == 1:
    num = int(input()) + int(input())
    print(f"Yes, value={num}")
else :
    for i in range(count):
        pairs.append(int(input()) + int(input()))

    if len(set(pairs))==1:
        print(f"Yes, value={pairs[0]}")
    else:
        for n in range(pairs.__len__()-1):
            check = math.fabs(pairs[n] - pairs[n+1])
            if check > maxdiff:
                maxdiff = check
        print(f"No, maxdiff={int(maxdiff)}")