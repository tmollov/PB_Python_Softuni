code = input()[::-1]
for ch in code:
    num = int(ch)
    if num == 0:
        print("ZERO")
        continue
    char = chr(num + 33)
    print(char * num)