import math

yearType = input()
holydays = int(input())
weekends = int(input())

games = ((48 - weekends) * (3/4)) + weekends
games += holydays * (2/3)

if yearType == "leap":
    games += (games * 0.15)

print(math.floor(games))