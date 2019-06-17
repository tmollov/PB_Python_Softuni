stairs = int(input())
rooms = int(input())

for i in range(rooms):
    print(f"L{stairs}{i}" ,end =" ")
print()

for i in range(stairs-1, 0 , -1):
    if i % 2 != 0:
        for n in range(rooms):
            print(f"A{i}{n}",end =" ")
        print()
    else :
        for n in range(rooms):
            print(f"O{i}{n}",end =" ")
        print()