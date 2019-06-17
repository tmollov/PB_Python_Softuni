n1 = int(input())
n2 = int(input())
operator = input()

if operator in ["+" , "-", "*"]:
    result = 0
    if operator == "+":
        result = n1+n2
    elif operator == "-" :
        result = n1 - n2
    else :
        result = n1 * n2
    isEven = result % 2 == 0
    if isEven:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")
elif operator == "/" :
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else :
        print(f"{n1} / {n2} = {n1/n2:.2f}")
else :
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else :
        print(f"{n1} % {n2} = {n1%n2}")
    