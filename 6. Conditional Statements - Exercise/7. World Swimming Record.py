import math

recordInSeconds = float(input())
rangeInMeters = float(input()) 
timeToSwimAMeter = float(input())


exp1 = (rangeInMeters * timeToSwimAMeter)
exp2 = rangeInMeters / 15
exp3 = math.floor(exp2) * 12.5
totalTime = exp1 + exp3
if totalTime >= recordInSeconds:
    print(f"No, he failed! He was {round(math.fabs(totalTime - recordInSeconds),2):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {round(totalTime,2):.2f} seconds.")