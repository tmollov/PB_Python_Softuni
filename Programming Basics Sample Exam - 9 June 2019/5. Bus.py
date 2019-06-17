passengers = int(input())
stops = int(input())

for i in range(1,stops+1):
    down = int(input())
    up = int(input())
    if i % 2 == 0:
        passengers -= down + 2
        passengers += up
    else :
        passengers += up + 2
        passengers -= down 

print(f"The final number of passengers is : {passengers}")