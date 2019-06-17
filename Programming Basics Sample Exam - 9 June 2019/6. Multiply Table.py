n = int(input())

a = int(n % 1000 / 100)
b = int(n % 100 / 10)
c = int(n % 10)

for i in range(1,c+1) :
    for j in range(1,b+1) :
        for k in range(1,a+1) :
            result = i*j*k
            print(f"{i} * {j} * {k} = {result};")