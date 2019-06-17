all = {"spring":9.5, "summer": 20, "winter":10}
girlBoy = {"spring":7.2, "summer": 15, "winter": 9.6}

girlSport = {"spring": "Athletics", "summer": "Volleyball", "winter": "Gymnastics"}
boySport =  {"spring": "Tennis", "summer": "Football", "winter": "Judo"}
mixedSport =  {"spring": "Cycling", "summer": "Swimming", "winter": "Ski"}

season = input().lower()
group = input().lower()
studentCount = int(input())
overnight = int(input()) 

sport = ""
price = 0
if group == "boys":
    sport += boySport[season]
    price = studentCount * overnight * girlBoy[season]
elif group == "girls" :
    sport += girlSport[season] 
    price = studentCount * overnight * girlBoy[season]
else :
    sport += mixedSport[season]
    price = studentCount * overnight * all[season]

if studentCount >= 10 and studentCount < 20:
    price -= price * 0.05
elif studentCount >= 20 and studentCount < 50:
    price -= price * 0.15
elif studentCount >= 50 :
    price -= price * 0.5

print(f'{sport} {price:.2f} lv.')