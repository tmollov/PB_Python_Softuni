from math import sqrt; from itertools import count, islice

primeNumSum = 0
nonprimeNumSum = 0

while True:
    num = input()
    if num == "stop":
        break
    num = int(num)
    if num < 0:
        print("Number is negative.")
        continue
    isPrime = num > 1 and all(num%i for i in islice(count(2), int(sqrt(num)-1)))
    if isPrime:
        primeNumSum += num
    else :
        nonprimeNumSum += num

print(f"Sum of all prime numbers is: {primeNumSum}")
print(f"Sum of all non prime numbers is: {nonprimeNumSum}")