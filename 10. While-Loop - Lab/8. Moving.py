length = int(input())
width = int(input())
height = int(input())
result = (length * width * height)
boxCount = 0
while True:
    command = input()
    if command == "Done" :
        print(f"{result-boxCount} Cubic meters left.")
        break
    boxCount += int(command)
    if boxCount > result :
        print(f'No more free space! You need {(result - boxCount) * -1} Cubic meters more.')
        break