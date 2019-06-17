totalTime = int(input()) + int(input()) + int(input())

seconds = totalTime % 60 
minutes = int(totalTime / 60) 

if  seconds < 10 : 
    seconds = '0' + str(seconds)

print(f"{minutes}:{seconds}")