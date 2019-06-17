hours = int(input())
mins = int(input()) + 15

if  mins / 60 >= 1:
    hours += 1
    mins -= 60

if  hours > 23 :
    hours -= 24

if mins < 10:
    mins = "0" + str(mins)

print(f"{hours}:{mins}")