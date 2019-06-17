start = int(input())
end = int(input())

for i in range(start, end + 1):
    n1 = int(i % 100000 / 10000)
    n2 = int(i % 10000 / 1000)
    n3 = int(i % 1000 / 100)
    n4 = int(i % 100 / 10)
    n5 = int(i % 10)
    left = n1+n2
    right = n4+n5
    if left> right:
        right += n3
    elif left < right:
        left += n3

    if left == right:
        print(i,end=" ")