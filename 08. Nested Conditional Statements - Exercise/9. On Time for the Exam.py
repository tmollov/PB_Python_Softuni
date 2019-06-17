import math

startExamHour = int(input())
startExamMinutes = int(input())
comeHour = int(input())
comeMinutes = int(input())

examTime = startExamHour * 60 + startExamMinutes
comeTime = comeHour * 60 + comeMinutes

lateTime = comeTime - examTime
earlyTime = examTime - comeTime

if lateTime > 0 :
    print("Late")
    if lateTime <= 59:
        print(f'{lateTime} minutes after the start')
    else :
        hours = int(lateTime / 60)
        minutes = lateTime % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif earlyTime >= 0 and earlyTime <= 30 :
    print("On time")
    if earlyTime != 0: 
        print(f'{earlyTime} minutes before the start')
elif earlyTime > 30 :
    print("Early")
    if earlyTime <= 59: 
        print(f"{earlyTime} minutes before the start")
    else :
        hours = int(earlyTime / 60)
        minutes = earlyTime % 60
        print(f"{hours}:{minutes:02d} hours before the start")

