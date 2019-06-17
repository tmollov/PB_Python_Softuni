width = int(input())
length = int(input())

sizeOfPasta = width * length
pieces = 0

while True:
    command = input()
    if command == "STOP":
        print(f"{sizeOfPasta - pieces} pieces are left.")
        break
    else:
        pieces += int(command)
        if pieces > sizeOfPasta:
            print(f"No more cake left! You need {pieces - sizeOfPasta} pieces more.")
            break