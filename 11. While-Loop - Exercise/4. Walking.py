steps = 0

while True:
    command = input()
    if command == "Going home":
        steps += int(input())
        if steps >= 10000:
            print("Goal reached! Good job!")
            break
        else:
            print(f"{10000 - steps} more steps to reach goal.")
            break
    else :
        steps += int(command)
        if steps >= 10000:
            print("Goal reached! Good job!")
            break