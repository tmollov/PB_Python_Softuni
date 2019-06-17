times = ["Hot", "Warm", "Mild", "Cool","Cold"]

t  = float(input())

if t >= 5.0 and t <= 11.9 :
    print(times[4])
elif t >= 12.0 and t <= 14.9:
    print(times[3])
elif t >= 15.0 and t <= 20.0:
    print(times[2])
elif t >= 20.1 and t <= 25.9:
    print(times[1])
elif t >= 26.0 and t <= 35.0:
    print(times[0])
else:
    print("unknown")