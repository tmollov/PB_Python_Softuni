start = int(input())
end = int(input())

for i in range(start, end + 1):
    n1 = int(i % 1000000 / 100000)
    n2 = int(i % 100000 / 10000)
    n3 = int(i % 10000 / 1000)
    n4 = int(i % 1000 / 100)
    n5 = int(i % 100 / 10)
    n6 = int(i % 10)
    if n1+n3+n5 == n2+n4+n6:
        print(i,end=" ")