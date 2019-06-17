balance = 0.0
counter = 1

payments = int(input())

while counter <= payments :
    number = float(input())
    if number >= 0:
        balance += number
        print(f"Increase: {number:.2f}")
    else :
        print("Invalid operation!")
        break
    counter += 1
print(f"Total: {balance:.2f}")