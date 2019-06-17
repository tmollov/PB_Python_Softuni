import math

firstBrother  = 1 / float(input())
secondBrother = 1 / float(input())
thirthBrother = 1 / float(input())
fishingTime = float(input())

time = 1 / (firstBrother+secondBrother+thirthBrother)
time *= 1.15

result = fishingTime - time
result = math.floor(result)

if result >= 0:
    print(f"Cleaning time: {time:.2f}")
    print(f"Yes, there is a surprise - time left -> {result} hours.")
else:
    print(f"Cleaning time: {time:.2f}")
    print(f"No, there isn't a surprise - shortage of time -> {math.fabs(result):.0f} hours.")
